# Import the required modules.
from modules import db
from modules import art


def createUserAttributesAndSkillsTable():
    # Create User Attributes and Skills Table
    connection = db.stdb()
    query = """CREATE TABLE `playersattribskills` (
		`pid` int(24) NOT NULL,
		`strength` int(3) NOT NULL,
		`endurance` int(3) NOT NULL,
		`intellect` int(3) NOT NULL,
		`dexterity` int(3) NOT NULL,
		`charisma` int(3) NOT NULL,
		`luck` int(3) NOT NULL,
		`psionicpotential` int(3) NOT NULL,
		`administration` int(3) NOT NULL,
		`artisticexpression` int(3) NOT NULL,
		`carousing` int(3) NOT NULL,
		`commsystemoperation` int(3) NOT NULL,
		`commsystemtechnology` int(3) NOT NULL,
		`computeroperation` int(3) NOT NULL,
		`computertechnology` int(3) NOT NULL,
		`damagecontrolprocedures` int(3) NOT NULL,
		`deflectorshieldoperation` int(3) NOT NULL,
		`deflectorshieldtechnology` int(3) NOT NULL,
		`electronicstechnology` int(3) NOT NULL,
		`environmentalsuitoperation` int(3) NOT NULL,
		`gaming` int(3) NOT NULL,
		`instruction` int(3) NOT NULL,
		`language` int(3) NOT NULL,
		`leadership` int(3) NOT NULL,
		`lifesciences` int(3) NOT NULL,
		`lsbionics` int(3) NOT NULL,
		`lsbotany` int(3) NOT NULL,
		`lsecology` int(3) NOT NULL,
		`lsexobiology` int(3) NOT NULL,
		`lsgenetics` int(3) NOT NULL,
		`lszoology` int(3) NOT NULL,
		`lifesupportsystemstechnology` int(3) NOT NULL,
		`marksmanshiparchaicweapon` int(3) NOT NULL,
		`marksmanshipmodernweapon` int(3) NOT NULL,
		`mechanicalengineering` int(3) NOT NULL,
		`medicalsciences` int(3) NOT NULL,
		`msgeneralmedicine` int(3) NOT NULL,
		`mspathology` int(3) NOT NULL,
		`mspsychology` int(3) NOT NULL,
		`mssurgery` int(3) NOT NULL,
		`negotiationanddiplomacy` int(3) NOT NULL,
		`personalcombatarmed` int(3) NOT NULL,
		`personalcombatunarmed` int(3) NOT NULL,
		`personalweaponstechnology` int(3) NOT NULL,
		`physicalsciences` int(3) NOT NULL,
		`pschemistry` int(3) NOT NULL,
		`pscomputerscience` int(3) NOT NULL,
		`psmathematics` int(3) NOT NULL,
		`psphysics` int(3) NOT NULL,
		`planetarysciences` int(3) NOT NULL,
		`plsgeology` int(3) NOT NULL,
		`plshydrology` int(3) NOT NULL,
		`plsmeteorology` int(3) NOT NULL,
		`planetarysurvival` int(3) NOT NULL,
		`securityprocedure` int(3) NOT NULL,
		`shuttlecraftpilot` int(3) NOT NULL,
		`shuttlecraftsystemstechnology` int(3) NOT NULL,
		`smallequipmentsystemsoperation` int(3) NOT NULL,
		`smallequipmentsystemstechnology` int(3) NOT NULL,
		`smallunittactics` int(3) NOT NULL,
		`socialsciences` int(3) NOT NULL,
		`ssarcheology` int(3) NOT NULL,
		`sseconomics` int(3) NOT NULL,
		`sslaw` int(3) NOT NULL,
		`sspoliticalscience` int(3) NOT NULL,
		`ssracialcultureandhistory` int(3) NOT NULL,
		`spacesciences` int(3) NOT NULL,
		`spsastrogation` int(3) NOT NULL,
		`spsastronautics` int(3) NOT NULL,
		`spsastronomy` int(3) NOT NULL,
		`spsastrophysics` int(3) NOT NULL,
		`sports` int(3) NOT NULL,
		`starshipcombatstrategyandtactics` int(3) NOT NULL,
		`starshiphelmoperation` int(3) NOT NULL,
		`starshipsensors` int(3) NOT NULL,
		`starshipweaponryoperation` int(3) NOT NULL,
		`starshipweaponrytechnology` int(3) NOT NULL,
		`streetwise` int(3) NOT NULL,
		`transporteroperationalprocedures` int(3) NOT NULL,
		`transporteroperationaltechnology` int(3) NOT NULL,
		`trivia` int(3) NOT NULL,
		`vehicleoperation` int(3) NOT NULL,
		`warpdrivetechnology` int(3) NOT NULL,
		`zerogoperations` int(3) NOT NULL
		)"""
    db.query(connection, query)

    connection = db.stdb()
    query = "ALTER TABLE `playersattribskills` ADD PRIMARY KEY (`pid`);"
    db.query(connection, query)

    connection = db.stdb()
    query = "ALTER TABLE `playersattribskills` MODIFY `pid` int(24) NOT NULL AUTO_INCREMENT;"
    db.query(connection, query)
