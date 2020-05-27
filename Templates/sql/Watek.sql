create table if not exists Watek(
                           id    integer primary key autoincrement,
                           temat varchar(30)                                                                 not null,
                           data_utworzenia date                                                              not null,
                           wyswietlenia int                                                                  not null,
                           kategoria integer                                                                 not null,
                           foreign key (kategoria) references Kategoria (id)
)