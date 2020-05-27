create table if not exists Post(
                           id    integer primary key autoincrement,
                           tresc varchar(1000)                                                               not null,
                           data_utworzenia timestamp                                                         not null,
                           watek integer                                                                     not null,
                           uzytkownik integer                                                                not null,
                           foreign key (watek) references Watek (id),
                           foreign key (uzytkownik) references Uzytkownik (id)
)