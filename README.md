### Documentation for deploy the app in macOS (w/Docker) ###

# Enter the Terminal
- Command + Spacebar, then write the word "Terminal" to execute it

# Install Homebrew
- Inside the Terminal, write:
    * /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
- Homebrew will need you to enter administrator credentials to download
- Verify that Homebrew is available in your PATH with:
    * echo 'eval "$(/opt/homebrew/bin/brew shellenv)"' >> ~/.zprofile
    * eval "$(/opt/homebrew/bin/brew shellenv)"

# Install Poetry
- Once Homebrew was succesfully installed, we have to install poetry in the Terminal:
    * brew install poetry

# Install Colima
- Next, we need to install Colima with the following line:
    * Standard instalation: brew install colima
    * Required instalation in this project: arch -arm64 brew install colima

# Initialize Docker
- Last step, the app needs to have docker installed:
    * brew install docker
    * brew install docker-compose
- When docker finish the download and instalation: initialize it with Colima:
    * colima start --with-docker