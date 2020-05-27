create table if not exists Kategoria(
                           id    integer primary key autoincrement,
                           nazwa varchar(30)                                                                 not null,
                           opis varchar(255)                                                                 not null
)