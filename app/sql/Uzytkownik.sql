create table if not exists Uzytkownik(
                           id    integer primary key autoincrement,
                           login text not null,
                           haslo text not null,
                           typ   text check (typ = 'Administrator' or typ = 'Moderator' or typ = 'Uzytkownik') not null
)