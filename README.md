# Universal Login CLI Program
## Requirements
You need docker to use this tool, then simply follow the usage guide

## Usage Guide
### Show help
```
docker run --rm ghabxph/ulcli:0.0.1 --help
```

### Interactive usage
Simply interact with the CLI tool when you directly run the cli through
docker
```
docker run --rm ghabxph/ulcli:0.0.1
```

### Using parameters (to minimize interactivity)
#### As mode=main/setup
You will run the below commands when you just initially deployed universal
login. Just change the values that fits your setup.
```
docker run --rm ghabxph/ulcli:0.0.1 \
  --url http://ul-domain.com:3001 main/setup \
  --db-host svc-nosql \
  --db-user root \
  --db-pass root \
  --db-name-prefix main_
```

#### As mode=main/get-token
Keep the token that the program will return to you.
```
docker run --rm ghabxph/ulcli:0.0.1 \
  --url http://ul-domain.com:3001 main/get-token \
  --username admin \
  --password admin
```

#### As mode=manage/setup
First, setup your manager instance by running the commands below
```
docker run --rm ghabxph/ulcli:0.0.1 \
  --url http://ul-domain.com:3011 manage/setup \
  --username admin \
  --password admin \
  --main-url <main-url-of-other-instance>
  --admin-token <token-here>
```

#### As mode=manager
This mode is simply manager mode after the manager/setup. This setup
atm is best used as interactive. When you run the command below, the
program shall collect inputs from you. Simply follow the output of
the program.
```
docker run --it --rm ghabxph/ulcli:0.0.1 \
  --url=http://ul-domain.com:3011 manage
```
