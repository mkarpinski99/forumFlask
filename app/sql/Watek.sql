create table if not exists Watek(
                           id    integer primary key autoincrement,
                           temat text not null,
                           data_utworzenia date not null,
                           wyswietlenia integer not null,
                           kategoria integer not null,
                           foreign key (kategoria) references Kategoria (id)
)