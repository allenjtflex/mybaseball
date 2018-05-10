BEGIN TRANSACTION;
CREATE TABLE IF NOT EXISTS `games_batresult` (
	`catcode`	varchar ( 2 ) NOT NULL,
	`description`	varchar ( 30 ) NOT NULL,
	`batseats`	integer NOT NULL,
	`batcount`	integer NOT NULL,
	PRIMARY KEY(`catcode`)
);
INSERT INTO `games_batresult` VALUES ('1B','安打',1,1);
INSERT INTO `games_batresult` VALUES ('2B','二壘安打',1,1);
INSERT INTO `games_batresult` VALUES ('3B','三壘安打',1,1);
INSERT INTO `games_batresult` VALUES ('HR','全壘打',1,1);
INSERT INTO `games_batresult` VALUES ('RR','場內全壘打',1,1);
INSERT INTO `games_batresult` VALUES ('GO','滾地球出局',1,1);
INSERT INTO `games_batresult` VALUES ('AO','飛球接殺',1,1);
INSERT INTO `games_batresult` VALUES ('FC','野手選擇上壘',1,1);
INSERT INTO `games_batresult` VALUES ('E','失誤上壘',1,1);
INSERT INTO `games_batresult` VALUES ('BB','四壞球',1,0);
INSERT INTO `games_batresult` VALUES ('DP','雙殺',1,1);
INSERT INTO `games_batresult` VALUES ('DB','觸身球',1,0);
INSERT INTO `games_batresult` VALUES ('K','三振',1,1);
INSERT INTO `games_batresult` VALUES ('KW','不死三振',1,1);
INSERT INTO `games_batresult` VALUES ('SH','犧牲觸擊',1,0);
INSERT INTO `games_batresult` VALUES ('SF','高飛犧牲打',1,0);
INSERT INTO `games_batresult` VALUES ('BT','短打',1,1);
COMMIT;
