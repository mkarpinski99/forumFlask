create table if not exists Uzytkownik(
                           id    integer primary key autoincrement,
                           login varchar(30)                                                                 not null,
                           haslo varchar(30)                                                                 not null,
                           typ   varchar(15) check (typ = 'Administrator' or typ = 'Moderator' or typ = 'Uzytkownik') not null
)