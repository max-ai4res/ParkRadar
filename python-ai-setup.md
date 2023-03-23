---------------------------------------------------------------------
--- PYHTON & PIP ---
---------------------------------------------------------------------
> install python 3.10 or more

> install pip
$ python -m pip install --upgrade pip

---------------------------------------------------------------------
--- GIT ---
---------------------------------------------------------------------
brew install git

---------------------------------------------------------------------
--- GITHUB ---
---------------------------------------------------------------------
# add SSH key to the GIT user

...> create a new key and add it to github.com in ~/.ssh
$ ssh-keygen -t ed25519 -C "your_email@example.com"

...> add ssh key to ssh-agent
$ eval "$(ssh-agent -s)"

...> change ~/.ssh/config to automatically load keys amd store passphrase 
in keychain

$open ~/.ssh/config

and add something like this:
Host *.github.com
  AddKeysToAgent yes
  UseKeychain yes
  IdentityFile ~/.ssh/id_ed25519

...> add yhe ssh private key to ssh-agent e store the passphrase into 
keychain

$ ssh-add --apple-use-keychain ~/.ssh/id_ed25519


...> and finally add ssh-key to github
https://docs.github.com/en/authentication/connecting-to-github-with-ssh/adding-a-new-ssh-key-to-your-github-account

...> TEST IT!
ssh -T git@github.com


---------------------------------------------------------------------
--- CLI ---
---------------------------------------------------------------------
> Install iTerm2
> Install OhMyZsh
> Install powerlevel10k

brew install romkatv/powerlevel10k/powerlevel10k
echo "source $(brew --prefix)/opt/powerlevel10k/powerlevel10k.zsh-theme" >>~/.zshrc
brew install zsh-syntax-highlighting

---------------------------------------------------------------------
-- packages --
---------------------------------------------------------------------
pip install torch   		// ML: machine leaning
pip install datasets 		// numeric and image data type support
pip install nltk		// natuaral language support
pip install matplotlib		// data visualization in python 
pip install numpy		// scientifc computing
pip install seaborn		// statistical data visualizzation

---------------------------------------------------------------------
-- how to setup an environment like this (I hope...) --
---------------------------------------------------------------------
conda activate myEnvName
conda env update --name myEnvName --file conda-environment.yml --prune
