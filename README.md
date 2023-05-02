# switchwon_admin

> **Notice**
> 환경 설정 시작전 해야할 것
> 1. Docker 를 설치 한다.
> 2. ".env" 파일을 생성한다. (링크 참고 : https://www.notion.so/env-3b3d85e28a4641939402a7f2ba3ebe37)
>

### Pycharm 환경 설정
1. Pycharm > Preference > Build, Execution, Development > Docker 를 선택 후, 아래와 같이 docker 를 추가한다.
   * Name 과 local path 는 알맞게 수정한다.
<img width="1000" alt="Screen Shot 2022-11-06 at 4 07 20 PM" src="https://user-images.githubusercontent.com/110358676/200195693-1cc98522-8ca6-4671-9d10-a0119b791299.png">

2. Interpreter settings 설정을 열고 Add interpreter > On docker compose 를 선택한다.
<img width="1335" alt="Screen Shot 2022-11-06 at 2 23 57 PM" src="https://user-images.githubusercontent.com/110358676/200195763-8467705e-6a57-44b2-934c-0810c52693ea.png">


3. 아래와 같이 (1) 에서 만든 Docker, 프로젝트 하위 docker-compose.yml, service 에 web 선택한 뒤  Next 를 누른다.
<img width="933" alt="Screen Shot 2022-11-06 at 2 51 51 PM" src="https://user-images.githubusercontent.com/110358676/200195738-6be6ea60-a494-408c-835f-fe50f4c84986.png">

4. 아래와 같이 install 이 완료 되면, Docker desktop 에서 재생 버튼을 눌러 (혹은 docker command 로) container 를 모두 실행 시켜준다. (Pycharm 에서 --no-start 로 실행되기 때문)
<img width="956" alt="Screen Shot 2022-11-06 at 3 53 26 PM" src="https://user-images.githubusercontent.com/110358676/200195795-c67aadf9-79b1-4125-9616-a1182f48b986.png">
<img width="1151" alt="Screen Shot 2022-11-06 at 3 53 33 PM" src="https://user-images.githubusercontent.com/110358676/200195806-fc974df5-bf95-4cd5-8836-ede9b23e4d69.png">

5. (4) 에서 Next 버튼을 누른뒤, create 버튼을 누르면, 아래와 같이 install package 가 추가 된다. Apply 를 누르고 OK 를 눌러 종료한다.
<img width="1042" alt="Screen Shot 2022-11-06 at 3 53 45 PM" src="https://user-images.githubusercontent.com/110358676/200196343-1382747e-a960-4e84-a41b-f861b87fdeb5.png">
<img width="1214" alt="Screen Shot 2022-11-06 at 3 31 39 PM" src="https://user-images.githubusercontent.com/110358676/200195850-0ca6b4cd-0d03-46ca-9d5f-cef45c8f9867.png">

6. http://127.0.0.1:WEB_PORT/docs#/ 를 실행 한다.
<img width="854" alt="Screen Shot 2022-11-06 at 4 23 23 PM" src="https://user-images.githubusercontent.com/110358676/200195880-0728c69d-3f0b-4743-b0f7-97a3af807ff0.png">

> **Notice**
> 웹 로그를 확인 하려면 Docker desktop 에서 switchwon_admin 컨테이터를 클릭해 Logs 에서 확인 하거나
> ```docker logs -f switchwon_admin``` 명령어를 terminal 에서 실행한다.

<img width="634" alt="Screen Shot 2022-11-06 at 4 03 56 PM" src="https://user-images.githubusercontent.com/110358676/200195906-4fc7e723-d0c8-4b52-9fa2-3965b3be18bb.png">
<img width="1072" alt="Screen Shot 2022-11-06 at 4 04 06 PM" src="https://user-images.githubusercontent.com/110358676/200195924-338e1121-29b5-4683-9aae-21434963799e.png">

OR

<img width="945" alt="Screen Shot 2022-11-06 at 4 30 04 PM" src="https://user-images.githubusercontent.com/110358676/200196188-9bb9988d-6234-413d-ac63-58e67e757aab.png">
