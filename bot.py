from aiohttp import (
    ClientResponseError,
    ClientSession,
    ClientTimeout,
    BasicAuth
)
from aiohttp_socks import ProxyConnector
from fake_useragent import FakeUserAgent
from http.cookies import SimpleCookie
from eth_account import Account
from eth_account.messages import encode_defunct
from eth_utils import to_hex
from datetime import datetime
from colorama import *
import asyncio, random, json, re, os, pytz

wib = pytz.timezone('Asia/Jakarta')

class Holmes:
    def __init__(self) -> None:
        self.BASE_API = "https://api.holmesai.xyz"
        self.REF_CODE = "p94lsFRp"
        self.HEADERS = {}
        self.proxies = []
        self.proxy_index = 0
        self.account_proxies = {}
        self.cookie_headers = {}
        self.device_fingerprints = {}
        
    def clear_terminal(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def log(self, message):
        print(
            f"{Fore.CYAN + Style.BRIGHT}[ {datetime.now().astimezone(wib).strftime('%x %X %Z')} ]{Style.RESET_ALL}"
            f"{Fore.WHITE + Style.BRIGHT} | {Style.RESET_ALL}{message}",
            flush=True
        )

    def welcome(self):
        print(
            f"""
        {Fore.GREEN + Style.BRIGHT}╔══════════════════════════════════════════════════════════╗
        ║     🚀 Holmes AI Auto Bot v2.0 - Multi Account     ║
        ║     🔒 Fingerprint Protection • Proxy Support       ║
        ╚══════════════════════════════════════════════════════════╝{Style.RESET_ALL}
            """
        )
        print(f"{Fore.YELLOW + Style.BRIGHT}➤ Reference Code: {self.REF_CODE}{Style.RESET_ALL}")

    def format_seconds(self, seconds):
        hours, remainder = divmod(seconds, 3600)
        minutes, seconds = divmod(remainder, 60)
        return f"{int(hours):02}:{int(minutes):02}:{int(seconds):02}"
    
    async def load_proxies(self):
        filename = "proxy.txt"
        try:
            if not os.path.exists(filename):
                self.log(f"{Fore.RED + Style.BRIGHT}✗ {Style.RESET_ALL}File {filename} not found")
                return
            with open(filename, 'r') as f:
                self.proxies = [line.strip() for line in f.read().splitlines() if line.strip()]
            
            if not self.proxies:
                self.log(f"{Fore.RED + Style.BRIGHT}✗ {Style.RESET_ALL}No proxies found")
                return

            self.log(
                f"{Fore.GREEN + Style.BRIGHT}✓ {Style.RESET_ALL}Loaded "
                f"{Fore.WHITE + Style.BRIGHT}{len(self.proxies)}{Style.RESET_ALL} proxies"
            )
        
        except Exception as e:
            self.log(f"{Fore.RED + Style.BRIGHT}✗ {Style.RESET_ALL}Failed to load proxies: {e}")
            self.proxies = []

    def check_proxy_schemes(self, proxies):
        schemes = ["http://", "https://", "socks4://", "socks5://"]
        if any(proxies.startswith(scheme) for scheme in schemes):
            return proxies
        return f"http://{proxies}"

    def get_next_proxy_for_account(self, account):
        if account not in self.account_proxies:
            if not self.proxies:
                return None
            proxy = self.check_proxy_schemes(self.proxies[self.proxy_index])
            self.account_proxies[account] = proxy
            self.proxy_index = (self.proxy_index + 1) % len(self.proxies)
        return self.account_proxies[account]

    def rotate_proxy_for_account(self, account):
        if not self.proxies:
            return None
        proxy = self.check_proxy_schemes(self.proxies[self.proxy_index])
        self.account_proxies[account] = proxy
        self.proxy_index = (self.proxy_index + 1) % len(self.proxies)
        return proxy
    
    def build_proxy_config(self, proxy=None):
        if not proxy:
            return None, None, None

        if proxy.startswith("socks"):
            connector = ProxyConnector.from_url(proxy)
            return connector, None, None

        elif proxy.startswith("http"):
            match = re.match(r"http://(.*?):(.*?)@(.*)", proxy)
            if match:
                username, password, host_port = match.groups()
                clean_url = f"http://{host_port}"
                auth = BasicAuth(username, password)
                return None, clean_url, auth
            else:
                return None, proxy, None

        raise Exception("Unsupported proxy type.")
        
    def generate_address(self, account: str):
        try:
            account = Account.from_key(account)
            address = account.address
            return address
        except Exception as e:
            return None
        
    def generate_payload(self, account: str, message: str):
        try:
            encoded_message = encode_defunct(text=message)
            signed_message = Account.sign_message(encoded_message, private_key=account)
            signature = to_hex(signed_message.signature)

            payload = {
                "Action": "Web3LoginVerifySign",
                "Signature": signature,
                "Message": message
            }

            return payload
        except Exception as e:
            raise Exception(f"Generate request payload failed: {str(e)}")
        
    def generate_tweet_prompt(self):
        topics = [
            "AI and Machine Learning", "Blockchain Technology", "Web3 Development", 
            "Cryptocurrency", "Cybersecurity", "Data Science", "Cloud Computing",
            "Software Development", "Digital Marketing", "Fintech Innovations",
            "NFT Ecosystem", "Metaverse", "DeFi Platforms", "Smart Contracts",
            "Digital Privacy", "Tech Startups", "Remote Work Tools", "Productivity Hacks",
            "Future of Work", "Digital Transformation", "IoT Devices", "5G Technology",
            "Edge Computing", "Quantum Computing", "AR/VR Technology", "Robotics",
            "Autonomous Vehicles", "Green Technology", "Sustainable Tech", "Health Tech",
            "EdTech Solutions", "AgriTech", "Smart Cities", "Digital Identity",
            "Tokenization", "DAO Governance", "Crypto Regulations", "Digital Assets",
            "Web Development", "Mobile Apps", "API Integration", "DevOps Practices",
            "UI/UX Design", "Game Development", "E-commerce Trends", "Social Media",
            "Content Creation", "Personal Branding", "Career Growth", "Entrepreneurship"
        ]
        
        styles = [
            "professional", "casual", "enthusiastic", "informative", "controversial",
            "optimistic", "critical", "humorous", "educational", "inspirational"
        ]
        
        topic = random.choice(topics)
        style = random.choice(styles)
        length = random.choice(["short", "medium", "long"])
        
        return f"Write a {style} tweet about {topic}. Make it {length}, engaging, and suitable for Twitter audience."

    def mask_account(self, account):
        try:
            if len(account) > 12:
                return account[:6] + '*' * 6 + account[-6:]
            return account
        except Exception as e:
            return "Invalid Address"

    def print_question(self):
        print(f"\n{Fore.YELLOW + Style.BRIGHT}🔧 Proxy Configuration:{Style.RESET_ALL}")
        print(f"{Fore.WHITE + Style.DIM}{'─'*50}{Style.RESET_ALL}")
        print(f"{Fore.CYAN + Style.BRIGHT}1.{Style.RESET_ALL} Run With Proxy")
        print(f"{Fore.CYAN + Style.BRIGHT}2.{Style.RESET_ALL} Run Without Proxy")
        print(f"{Fore.WHITE + Style.DIM}{'─'*50}{Style.RESET_ALL}")
        
        while True:
            try:
                proxy_choice = int(input(f"\n{Fore.GREEN + Style.BRIGHT}➤{Style.RESET_ALL} Select option [1/2]: ").strip())

                if proxy_choice in [1, 2]:
                    proxy_type = "With" if proxy_choice == 1 else "Without"
                    self.log(f"{Fore.GREEN + Style.BRIGHT}✓{Style.RESET_ALL} Running {proxy_type} proxy")
                    break
                else:
                    self.log(f"{Fore.RED + Style.BRIGHT}✗{Style.RESET_ALL} Please enter 1 or 2")
            except ValueError:
                self.log(f"{Fore.RED + Style.BRIGHT}✗{Style.RESET_ALL} Invalid input. Enter a number (1 or 2)")

        rotate_proxy = False
        if proxy_choice == 1:
            while True:
                rotate_input = input(f"{Fore.GREEN + Style.BRIGHT}➤{Style.RESET_ALL} Rotate invalid proxies? [y/n]: ").strip().lower()
                if rotate_input in ["y", "n"]:
                    rotate_proxy = rotate_input == "y"
                    if rotate_proxy:
                        self.log(f"{Fore.YELLOW + Style.BRIGHT}⚠{Style.RESET_ALL} Proxy rotation enabled")
                    else:
                        self.log(f"{Fore.YELLOW + Style.BRIGHT}⚠{Style.RESET_ALL} Proxy rotation disabled")
                    break
                else:
                    self.log(f"{Fore.RED + Style.BRIGHT}✗{Style.RESET_ALL} Enter 'y' or 'n'")

        return proxy_choice, rotate_proxy
    
    def generate_fingerprint_headers(self, address: str):
        """Generate unique fingerprint headers for each account"""
        if address not in self.device_fingerprints:
            # Generate or fetch from persistent storage
            faker = FakeUserAgent()
            user_agent = faker.random
            
            # Generate device fingerprint
            device_id = f"device_{random.randint(100000, 999999)}_{int(datetime.now().timestamp())}"
            
            # Browser fingerprints
            browser_families = ["Chrome", "Firefox", "Safari", "Edge", "Opera"]
            browser = random.choice(browser_families)
            
            # Platform fingerprints
            platforms = ["Windows NT 10.0", "Macintosh; Intel Mac OS X 10_15_7", "X11; Linux x86_64"]
            platform = random.choice(platforms)
            
            self.device_fingerprints[address] = {
                "device_id": device_id,
                "browser": browser,
                "platform": platform,
                "user_agent": user_agent
            }
        
        fingerprint = self.device_fingerprints[address]
        
        return {
            "Accept": "*/*",
            "Accept-Language": random.choice(["en-US,en;q=0.9", "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"]),
            "Accept-Encoding": "gzip, deflate, br",
            "Connection": "keep-alive",
            "Host": "api.holmesai.xyz",
            "Origin": "https://www.holmesai.xyz",
            "Referer": "https://www.holmesai.xyz/",
            "Sec-Fetch-Dest": "empty",
            "Sec-Fetch-Mode": "cors",
            "Sec-Fetch-Site": "same-site",
            "User-Agent": fingerprint["user_agent"],
            "X-Device-ID": fingerprint["device_id"],
            "X-Client-Type": "web",
            "X-Client-Version": f"{random.randint(1, 3)}.{random.randint(0, 9)}.{random.randint(0, 9)}"
        }
    
    async def check_connection(self, proxy_url=None):
        connector, proxy, proxy_auth = self.build_proxy_config(proxy_url)
        try:
            async with ClientSession(connector=connector, timeout=ClientTimeout(total=30)) as session:
                async with session.get(url="https://api.ipify.org?format=json", proxy=proxy, proxy_auth=proxy_auth) as response:
                    response.raise_for_status()
                    data = await response.json()
                    ip = data.get("ip", "Unknown")
                    self.log(f"{Fore.GREEN + Style.BRIGHT}✓{Style.RESET_ALL} Connection test passed | IP: {ip}")
                    return True
        except (Exception, ClientResponseError) as e:
            self.log(
                f"{Fore.RED + Style.BRIGHT}✗{Style.RESET_ALL} Connection test failed: {str(e)[:50]}"
            )
        
        return False
    
    async def get_message(self, address: str, proxy_url=None, retries=5):
        url = f"{self.BASE_API}/api"
        data = json.dumps({"Action": "Web3LoginGetMessage", "Address": address})
        headers = {
            **self.HEADERS[address],
            "Content-Length": str(len(data)),
            "Content-Type": "application/json"
        }
        for attempt in range(retries):
            connector, proxy, proxy_auth = self.build_proxy_config(proxy_url)
            try:
                async with ClientSession(connector=connector, timeout=ClientTimeout(total=60)) as session:
                    async with session.post(url=url, headers=headers, data=data, proxy=proxy, proxy_auth=proxy_auth, allow_redirects=False) as response:
                        response.raise_for_status()
                        raw_cookies = response.headers.getall('Set-Cookie', [])
                        for ck in raw_cookies:
                            if "yott_ai_session" in ck:
                                cookie = SimpleCookie()
                                cookie.load("\n".join(raw_cookies))
                                cookie_string = "; ".join([f"{key}={morsel.value}" for key, morsel in cookie.items()])
                                self.cookie_headers[address] = cookie_string

                                return await response.json()
            except (Exception, ClientResponseError) as e:
                if attempt < retries - 1:
                    await asyncio.sleep(5)
                    continue
                self.log(
                    f"{Fore.RED + Style.BRIGHT}✗{Style.RESET_ALL} Fetch message failed: {str(e)[:50]}"
                )

        return None
    
    async def verify_sign(self, account: str, address: str, message: str, proxy_url=None, retries=5):
        url = f"{self.BASE_API}/api"
        data = json.dumps(self.generate_payload(account, message))
        headers = {
            **self.HEADERS[address],
            "Content-Length": str(len(data)),
            "Content-Type": "application/json",
            "Cookie": self.cookie_headers[address]
        }
        for attempt in range(retries):
            connector, proxy, proxy_auth = self.build_proxy_config(proxy_url)
            try:
                async with ClientSession(connector=connector, timeout=ClientTimeout(total=60)) as session:
                    async with session.post(url=url, headers=headers, data=data, proxy=proxy, proxy_auth=proxy_auth, allow_redirects=False) as response:
                        raw_cookies = response.headers.getall('Set-Cookie', [])
                        for ck in raw_cookies:
                            if "login_yott_ai" in ck:
                                cookie = SimpleCookie()
                                cookie.load("\n".join(raw_cookies))
                                cookie_string = "; ".join([f"{key}={morsel.value}" for key, morsel in cookie.items()])
                                self.cookie_headers[address] = cookie_string

                                return True
            except (Exception, ClientResponseError) as e:
                if attempt < retries - 1:
                    await asyncio.sleep(5)
                    continue
                self.log(
                    f"{Fore.RED + Style.BRIGHT}✗{Style.RESET_ALL} Login failed: {str(e)[:50]}"
                )

        return None
    
    async def get_user(self, address: str, proxy_url=None, retries=5):
        url = f"{self.BASE_API}/agent-service"
        data = json.dumps({"Action": "GetUser", "InviteCode": self.REF_CODE})
        headers = {
            **self.HEADERS[address],
            "Content-Length": str(len(data)),
            "Content-Type": "application/json",
            "Cookie": self.cookie_headers[address]
        }
        for attempt in range(retries):
            connector, proxy, proxy_auth = self.build_proxy_config(proxy_url)
            try:
                async with ClientSession(connector=connector, timeout=ClientTimeout(total=60)) as session:
                    async with session.post(url=url, headers=headers, data=data, proxy=proxy, proxy_auth=proxy_auth) as response:
                        response.raise_for_status()
                        return await response.json()
            except (Exception, ClientResponseError) as e:
                if attempt < retries - 1:
                    await asyncio.sleep(5)
                    continue
                self.log(
                    f"{Fore.RED + Style.BRIGHT}✗{Style.RESET_ALL} Fetch user data failed: {str(e)[:50]}"
                )

        return None
    
    async def daily_checkin(self, address: str, proxy_url=None, retries=5):
        url = f"{self.BASE_API}/agent-service"
        data = json.dumps({"Action": "CheckIn", "UserId": address})
        headers = {
            **self.HEADERS[address],
            "Content-Length": str(len(data)),
            "Content-Type": "application/json",
            "Cookie": self.cookie_headers[address]
        }
        for attempt in range(retries):
            connector, proxy, proxy_auth = self.build_proxy_config(proxy_url)
            try:
                async with ClientSession(connector=connector, timeout=ClientTimeout(total=60)) as session:
                    async with session.post(url=url, headers=headers, data=data, proxy=proxy, proxy_auth=proxy_auth) as response:
                        response.raise_for_status()
                        return await response.json()
            except (Exception, ClientResponseError) as e:
                if attempt < retries - 1:
                    await asyncio.sleep(5)
                    continue
                self.log(
                    f"{Fore.RED + Style.BRIGHT}✗{Style.RESET_ALL} Daily check-in failed: {str(e)[:50]}"
                )

        return None
    
    async def agent_list(self, address: str, proxy_url=None, retries=5):
        url = f"{self.BASE_API}/agent-service"
        data = json.dumps({"Action": "GetUserAgentList", "UserId": address})
        headers = {
            **self.HEADERS[address],
            "Content-Length": str(len(data)),
            "Content-Type": "application/json",
            "Cookie": self.cookie_headers[address]
        }
        for attempt in range(retries):
            connector, proxy, proxy_auth = self.build_proxy_config(proxy_url)
            try:
                async with ClientSession(connector=connector, timeout=ClientTimeout(total=60)) as session:
                    async with session.post(url=url, headers=headers, data=data, proxy=proxy, proxy_auth=proxy_auth) as response:
                        response.raise_for_status()
                        return await response.json()
            except (Exception, ClientResponseError) as e:
                if attempt < retries - 1:
                    await asyncio.sleep(5)
                    continue
                self.log(
                    f"{Fore.RED + Style.BRIGHT}✗{Style.RESET_ALL} Fetch agent list failed: {str(e)[:50]}"
                )

        return None
    
    async def instant_generate(self, address: str, agent_id: int, prompt: str, proxy_url=None, retries=5):
        url = f"{self.BASE_API}/agent-backend/instant_generate"
        data = json.dumps({"agent_id": agent_id, "chat_history": [], "prompt": prompt})
        headers = {
            **self.HEADERS[address],
            "Content-Length": str(len(data)),
            "Content-Type": "application/json",
            "Cookie": self.cookie_headers[address]
        }
        for attempt in range(retries):
            connector, proxy, proxy_auth = self.build_proxy_config(proxy_url)
            try:
                async with ClientSession(connector=connector, timeout=ClientTimeout(total=60)) as session:
                    async with session.post(url=url, headers=headers, data=data, proxy=proxy, proxy_auth=proxy_auth) as response:
                        response.raise_for_status()
                        return await response.json()
            except (Exception, ClientResponseError) as e:
                if attempt < retries - 1:
                    await asyncio.sleep(5)
                    continue
                self.log(
                    f"{Fore.RED + Style.BRIGHT}✗{Style.RESET_ALL} Instant generate failed: {str(e)[:50]}"
                )

        return None
    
    async def create_workflow(self, address: str, agent_id: int, output: str, proxy_url=None, retries=5):
        url = f"{self.BASE_API}/agent-service"
        data = json.dumps({"Action": "CreateWorkflowResults", "AgentId": agent_id, "Title":"Instant Generate", "Content": output})
        headers = {
            **self.HEADERS[address],
            "Content-Length": str(len(data)),
            "Content-Type": "application/json",
            "Cookie": self.cookie_headers[address]
        }
        for attempt in range(retries):
            connector, proxy, proxy_auth = self.build_proxy_config(proxy_url)
            try:
                async with ClientSession(connector=connector, timeout=ClientTimeout(total=60)) as session:
                    async with session.post(url=url, headers=headers, data=data, proxy=proxy, proxy_auth=proxy_auth) as response:
                        response.raise_for_status()
                        return await response.json()
            except (Exception, ClientResponseError) as e:
                if attempt < retries - 1:
                    await asyncio.sleep(5)
                    continue
                self.log(
                    f"{Fore.RED + Style.BRIGHT}✗{Style.RESET_ALL} Publish failed: {str(e)[:50]}"
                )

        return None
    
    async def process_check_connection(self, address: str, use_proxy: bool, rotate_proxy: bool):
        while True:
            proxy = self.get_next_proxy_for_account(address) if use_proxy else None
            if proxy:
                self.log(f"{Fore.CYAN + Style.BRIGHT}🔌{Style.RESET_ALL} Using proxy: {proxy[:50]}...")

            is_valid = await self.check_connection(proxy)
            if not is_valid:
                if rotate_proxy and proxy:
                    self.log(f"{Fore.YELLOW + Style.BRIGHT}🔄{Style.RESET_ALL} Rotating proxy...")
                    proxy = self.rotate_proxy_for_account(address)
                    await asyncio.sleep(1)
                    continue
                return False

            return True
    
    async def process_user_login(self, account: str, address: str, use_proxy: bool, rotate_proxy: bool):
        is_valid = await self.process_check_connection(address, use_proxy, rotate_proxy)
        if is_valid:
            proxy = self.get_next_proxy_for_account(address) if use_proxy else None

            get_message = await self.get_message(address, proxy)
            if not get_message: 
                return False

            message = get_message.get("Message")
            self.log(f"{Fore.CYAN + Style.BRIGHT}📝{Style.RESET_ALL} Message to sign: {message[:50]}...")

            verify = await self.verify_sign(account, address, message, proxy)
            if not verify: 
                return False

            self.log(f"{Fore.GREEN + Style.BRIGHT}✅{Style.RESET_ALL} Login successful")
            return True
        return False

    async def process_accounts(self, account: str, address: str, use_proxy: bool, rotate_proxy: bool):
        logined = await self.process_user_login(account, address, use_proxy, rotate_proxy)
        if logined:
            proxy = self.get_next_proxy_for_account(address) if use_proxy else None

            user = await self.get_user(address, proxy)
            if user:
                if user.get("RetCode") == 0:
                    points = user.get("Points")
                    has_checkin = user.get("CheckinDone")

                    self.log(f"{Fore.YELLOW + Style.BRIGHT}💰{Style.RESET_ALL} Points: {points} Clue")

                    if not has_checkin:
                        checkin = await self.daily_checkin(address, proxy)
                        if checkin:
                            if checkin.get("RetCode") == 0:
                                self.log(f"{Fore.GREEN + Style.BRIGHT}✅{Style.RESET_ALL} Daily check-in successful")
                            else:
                                message = checkin.get("Message")
                                self.log(f"{Fore.RED + Style.BRIGHT}✗{Style.RESET_ALL} Check-in failed: {message}")
                    else:
                        self.log(f"{Fore.CYAN + Style.BRIGHT}ℹ{Style.RESET_ALL} Already checked in today")
                else:
                    message = user.get("Message")
                    self.log(f"{Fore.RED + Style.BRIGHT}✗{Style.RESET_ALL} User data error: {message}")

            agent_lists = await self.agent_list(address, proxy)
            if agent_lists:
                if agent_lists.get("RetCode") == 0:
                    agents = agent_lists.get("Agents", [])

                    if agents == []:
                        self.log(f"{Fore.YELLOW + Style.BRIGHT}⚠{Style.RESET_ALL} No agent found. Create one manually first.")
                    else:
                        self.log(f"{Fore.CYAN + Style.BRIGHT}🤖{Style.RESET_ALL} Found {len(agents)} agent(s)")
                        agent_id = agents[0]["Id"]
                        prompt = self.generate_tweet_prompt()

                        self.log(f"{Fore.BLUE + Style.BRIGHT}➤{Style.RESET_ALL} Agent ID: {agent_id}")
                        self.log(f"{Fore.BLUE + Style.BRIGHT}➤{Style.RESET_ALL} Prompt: {prompt[:80]}...")

                        generate = await self.instant_generate(address, agent_id, prompt, proxy)
                        if generate:
                            if generate.get("success", False):
                                output = generate.get("output")

                                self.log(f"{Fore.BLUE + Style.BRIGHT}➤{Style.RESET_ALL} Output generated: {output[:80]}...")

                                publish = await self.create_workflow(address, agent_id, output, proxy)
                                if publish:
                                    if publish.get("RetCode") == 0:
                                        self.log(f"{Fore.GREEN + Style.BRIGHT}✅{Style.RESET_ALL} Published successfully")
                                    else:
                                        message = publish.get("Message")
                                        self.log(f"{Fore.RED + Style.BRIGHT}✗{Style.RESET_ALL} Publish failed: {message}")
                            else:
                                self.log(f"{Fore.RED + Style.BRIGHT}✗{Style.RESET_ALL} Generate failed")

                else:
                    message = agent_lists.get("Message")
                    self.log(f"{Fore.RED + Style.BRIGHT}✗{Style.RESET_ALL} Agent list error: {message}")

    async def main(self):
        try:
            with open('accounts.txt', 'r') as file:
                accounts = [line.strip() for line in file if line.strip()]

            proxy_choice, rotate_proxy = self.print_question()

            while True:
                self.clear_terminal()
                self.welcome()
                self.log(f"{Fore.GREEN + Style.BRIGHT}📊{Style.RESET_ALL} Total accounts: {len(accounts)}")

                use_proxy = True if proxy_choice == 1 else False
                if use_proxy:
                    await self.load_proxies()

                print(f"\n{Fore.YELLOW + Style.BRIGHT}🚀 Processing Accounts:{Style.RESET_ALL}")
                print(f"{Fore.WHITE + Style.DIM}{'─'*60}{Style.RESET_ALL}")

                for idx, account in enumerate(accounts, start=1):
                    if account:
                        address = self.generate_address(account)
                        print(f"\n{Fore.CYAN + Style.BRIGHT}[ Account {idx}/{len(accounts)} ]{Style.RESET_ALL}")
                        self.log(f"{Fore.WHITE + Style.BRIGHT}Address: {self.mask_account(address)}")

                        if not address:
                            self.log(f"{Fore.RED + Style.BRIGHT}✗{Style.RESET_ALL} Invalid private key")
                            continue

                        # Generate unique fingerprint headers for this account
                        self.HEADERS[address] = self.generate_fingerprint_headers(address)
                        self.log(f"{Fore.CYAN + Style.BRIGHT}🆔{Style.RESET_ALL} Fingerprint generated")

                        await self.process_accounts(account, address, use_proxy, rotate_proxy)
                        
                        print(f"{Fore.WHITE + Style.DIM}{'─'*60}{Style.RESET_ALL}")

                self.log(f"{Fore.GREEN + Style.BRIGHT}✅{Style.RESET_ALL} All accounts processed")
                
                # Wait for next cycle (24 hours)
                delay = 24 * 60 * 60
                self.log(f"{Fore.CYAN + Style.BRIGHT}⏳{Style.RESET_ALL} Next cycle in 24 hours")
                
                while delay > 0:
                    formatted_time = self.format_seconds(delay)
                    print(
                        f"{Fore.CYAN + Style.BRIGHT}[ {Style.RESET_ALL}"
                        f"{Fore.WHITE + Style.BRIGHT}⏰ {formatted_time}{Style.RESET_ALL}"
                        f"{Fore.CYAN + Style.BRIGHT} ]{Style.RESET_ALL}"
                        f" Waiting for next cycle...",
                        end="\r",
                        flush=True
                    )
                    await asyncio.sleep(1)
                    delay -= 1
                
                print()  # New line after countdown

        except FileNotFoundError:
            self.log(f"{Fore.RED + Style.BRIGHT}✗{Style.RESET_ALL} File 'accounts.txt' not found")
            return
        except Exception as e:
            self.log(f"{Fore.RED + Style.BRIGHT}💥{Style.RESET_ALL} Error: {str(e)}")
            raise e

if __name__ == "__main__":
    try:
        bot = Holmes()
        asyncio.run(bot.main())
    except KeyboardInterrupt:
        print(f"\n\n{Fore.YELLOW + Style.BRIGHT}👋{Style.RESET_ALL} Exiting Holmes AI Bot...")
