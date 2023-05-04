# fastapi & tortoise skeleton

> **Notice**  
> Before starting setting up
> 1. Install Docker on your local.
> 2. Create .env file like below.
>> DB_URL="mysql://mysqluser:mysqluser@local-db:3306"  
TOKEN_KEY="UDg8RZIWnnOgXf2SWemX0V+4mcSrN5Nyu2MjLKwwJJQ="   
AES_KEY="testaeskey"
>

### Pycharm 환경 설정
1. Go to Pycharm > Preference > Build, Execution, Development > Docker, add docker.

2. Open "Interpreter settings" then click Add interpreter > On docker compose.

3. Choose Docker we made from (1) and docker-compose.yml under project file, service > web then go to the Next.

4. After docker compose succeed, Start docker container start using Docker desktop GUI or docker command. (Pycharm use --no-start option)

5. After processing (4) click Next button. Here you should set python path. Click "..." button and then set path: /usr/local/bin/python3
then choose the python path and click Create button.

6. Check swagger docs http://127.0.0.1:8005/docs#/.

