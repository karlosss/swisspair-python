#include <pybind11/pybind11.h>
#include <pybind11/stl.h>
#include <iostream>
#include <set>
#include <vector>

namespace py = pybind11;

struct Player {
  std::string id;
  std::set<std::string> cannot_be_paired_against_ids;
  bool can_get_bye = true;
  int points;
  int rank;

  std::string to_string() const;

  bool operator==(const Player& other) const;
};

struct Match {
  Player p1;
  Player p2;
  bool is_bye;

  Match(const Player & p1, const Player & p2);
  Match(const Player & p1);
  Match(const Match & other);

  bool operator<(const Match & other) const;


  std::string to_string() const;
};

std::vector<Match> create_matches(const std::vector<Player>& players, bool powerPairing);


PYBIND11_MODULE(_swisspair, m) {
    m.doc() = "Swiss pairing algorithm for not only Magic: The Gathering";

    py::class_<Player>(m, "Player")
        .def(py::init<>())
        .def_readwrite("id", &Player::id)
        .def_readwrite("cannot_be_paired_against_ids", &Player::cannot_be_paired_against_ids)
        .def_readwrite("can_get_bye", &Player::can_get_bye)
        .def_readwrite("points", &Player::points)
        .def_readwrite("rank", &Player::rank);

    py::class_<Match>(m, "Match")
        .def_readonly("p1", &Match::p1)
        .def_readonly("p2", &Match::p2)
        .def_readonly("is_bye", &Match::is_bye);

    m.def("create_matches", &create_matches, "Creates a list of matches, ordered by the table number from the highest table. Power pairing guarantees the top 8 players to be paired according to their standing.");
}