create table if not exists Kategoria(
                           id    integer primary key autoincrement,
                           nazwa text not null,
                           opis text not null
)