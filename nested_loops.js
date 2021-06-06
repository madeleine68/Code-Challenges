//create a script that creates 5 teams of 4 people and assign
// a unique identifier to each team member. The script should display 
//the team number, person number, and identifier for that 
//person/team. avoid displaying zeros(e.g. team 0, player 0)
var id = 1
for (var team = 1; team < 6 ; team++) {
    for (player = 1; player < 5; player++) {
         gs.info("team " +team +" palyer " + player + " id " +id)
         id++
    }
}