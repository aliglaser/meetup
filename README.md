On Dev Branch: simple chat webapp - just for stepping bridge

---------------------------------------------------------------------

# Teaming

## Concept

Minimalized Make-team-webapp based on django. Anyone can simply sign in using their sns account or email, make or join any team they wnat, and go play!

## Reqirement

### Pypi

django, channels, channels_redis, social-auth-app-django

### Others

Redis-server

    $ sudo apt install redis-server

Or you can use docker if you want.

### Docker

Redis ( recommanded: you can use newer version of redis server with docker )

Mysql: 5.5 or higher ( but latest mysql version(v8) doesn't work with phpmyadmin docker this time ).

    docker run -d \
    --name teaming-mysql \
    -e MYSQL_ROOT_PASSWORD=admin \
    -p 3306:3306 \
    mysql:5

(Optional) phpmyadmin

    docker run -d \
    --name teaming-myadmin \
    --link teaming-mysql:db \
    -p 8080:80 \
    phpmyadmin/phpmyadmin

And easily access mysql db with root/admin account.


## Model - Room, User

### Room 

- id: int
'PositiveIntegerField'

- user: ['John', 'jane', ...] if empty, don't display on list

- limit: int
'PositiveIntegerField'
- tag: ['python', 'C#', ....]
- chat_log: list { user: , time: , chat: }
- age: {min: , max: }
- date: {cerated: , last_activity: }
- location: Seoul Joong-gu

No private, only public. anyone can lookup rooms
tag filtering needs
Room exposure fee on top
Room order: created date.


### TEAMINGUser : Uesr model - keyword is already being used.

- profile image: server upload
'URLField'
- name: string
'CharField'
- id: email
'EmailField'
- auth: password
- introduce info: string
'CharField'
- nationality: Country string
- age: int
- tag: list string - Room's tag
- room: joined room list
- recent access ip:

