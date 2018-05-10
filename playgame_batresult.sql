BEGIN TRANSACTION;
CREATE TABLE IF NOT EXISTS `playgame_batresult` (
	`catcode`	varchar ( 2 ) NOT NULL,
	`description`	varchar ( 30 ) NOT NULL,
	`batseats`	integer NOT NULL,
	`batcount`	integer NOT NULL,
	PRIMARY KEY(`catcode`)
);
COMMIT;
