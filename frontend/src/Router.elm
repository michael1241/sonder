module Router exposing (..)

import Url.Parser as URLParser exposing (Parser, (</>), int, map, oneOf, s, string)


type Route
    = Login
    | Unauthorized
    | Dashboard
    | PlayerList


routeParser : Parser (Route -> a) a
routeParser =
    oneOf
        [ map Login (s "login")
        , map Dashboard (s "dashboard")
        , map PlayerList (s "players")
        , map Unauthorized (s "login" </> s "unauthorized")
        ]


parse =
    URLParser.parse
