Hello Bug Bashers! This is Arvin and following is a guide to follow in order to contribute on development.


PRELIMINARY INFORMATION
    This guide is created by me and therefore created based on my system. There should not be any conflicts,
    however details like my OS and hardware may have an impact on how you follow this guide. The documentation
    provided should have information on how to configure your settings based on your needs. That said, my specs:

        OS: 
            Windows 11 Pro
                - Version:  23H2
                - OS Build: 22631.3155
        Hardware:
            - CPU: Intel i7 13700k
            - GPU: Nvidia RTX 4090 MSI Trio
            - RAM: Corsair Dominator 64gb DDR5 5600MHz

SETUP
    We will be using a variety of tools, the following will be a guide on how to install those tools. Keep in mind,
    it's best practice to setup a virtual enviroment so the packages we install are all on the root of our project
    folder. I am going to use Poetry for the virtual enviroment over the built in venv, I'll be providing steps on
    setting that up too.

    GLOBAL
        - Install Python: https://www.python.org/downloads/
            - I'm running version 3.12.2, latest as of 3/02/2024
            - I checked "use admin privileges when installing py.exe" and "add to PATH". Unsure if this will be
            important, I am documenting it incase we run into an issue.       
        - Install VsCode: https://code.visualstudio.com/
            - Alternativly, you can install it using the Microsoft store as I did.
        - Install Git: https://git-scm.com/book/en/v2/Getting-Started-Installing-Git
            - Download the version for your OS.
            - Install it, during setup I changed the default editor to VsCode. As I understand it, this is just
            personal preference and shouldn't impact the project.
        - Install Node.js: https://nodejs.org/en
            - I enabled "Automaticlly install the necessary tools..." during setup.
        - Install Poetry: https://pypi.org/project/poetry/
            - When installing pipx (the link has another link to install that), take out --user. Otherwise you will
            install it under ROAMING which then makes yous you add that directory to the PATH. Should be fine but
            I couldn't get it realize the PATH so I just installed it under LOCAL
            - I used elevated CMD and ran 'pipx install poetry', then CMD made me run 'pipx ensurepath'
        - Open VsCode, install a few extensions (you can copy the ID into the extension marketplace):
            - Python: ms-python.python
            - GitHub Codespaces: GitHub.codespaces
            - MongoDB for VS Code: mongodb.mongodb-vscode
    
    LOCAL
        - Open Source Control(or press CTRL+SHIFT+G)
        - 
        - If you need to configure your account, enter the following into the command prompt:
            - git config –global user.name “Your GitHub username”
            - git config –global user.email “Your email”