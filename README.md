# Teaming

## Rayout

![](teaming/teaming_layout/New Mockup 1.png)

![](teaming/teaming_layout/New Mockup 2.png)

![](teaming/teaming_layout/New Mockup 3.png)

![](teaming/teaming_layout/New Mockup 4.png)

![](teaming/teaming_layout/New Mockup 5.png)

![](teaming/teaming_layout/New Mockup 1.png)

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


### User

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

