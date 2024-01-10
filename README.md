Control your TP-Link Tapo Devices through CLI.

- Clone this repository

```shell
git clone https://gitlab.com/strawberry-soda/tp-link-tapo-cli.git
```

- Install the required libraries

```shell
pip install -r requirements.txt
```

- Configure the .env

```shell
cp .env.example .env
```

- Open the .env file and replace the email and password values with the credentials you use to log into the Tapo app

### Usage

Run `python main.py -h` to see the usage

### Example

Turn on the light (Tapo L530 Bulb)

```shell
python main.py --type light --ip 192.168.xxx.xxx --on
```

To check your Tapo device IP address, go to your device **settings** > **device info**
