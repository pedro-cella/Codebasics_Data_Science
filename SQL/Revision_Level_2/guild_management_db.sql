-- =====================================================
-- guild_management_db.sql
-- RPG Guild Management Database
-- MySQL compatible | InnoDB | UTF8MB4
-- =====================================================

DROP DATABASE IF EXISTS guild_management_db;
CREATE DATABASE guild_management_db
  CHARACTER SET utf8mb4
  COLLATE utf8mb4_unicode_ci;
USE guild_management_db;

-- =====================================================
-- TABLE CREATION
-- =====================================================

CREATE TABLE adventurers (
    adventurer_id INT          NOT NULL,
    name          VARCHAR(100) NOT NULL,
    class         VARCHAR(50)  NOT NULL,
    `rank`        VARCHAR(50)  NOT NULL,
    `level`       INT          NOT NULL,
    join_date     DATE         NOT NULL,
    PRIMARY KEY (adventurer_id)
) ENGINE=InnoDB;

CREATE TABLE guilds (
    guild_id   INT          NOT NULL,
    guild_name VARCHAR(100) NOT NULL,
    region     VARCHAR(100) NOT NULL,
    PRIMARY KEY (guild_id)
) ENGINE=InnoDB;

CREATE TABLE adventurer_guild (
    adventurer_id     INT  NOT NULL,
    guild_id          INT  NOT NULL,
    joined_guild_date DATE NOT NULL,
    PRIMARY KEY (adventurer_id, guild_id),
    CONSTRAINT fk_ag_adventurer FOREIGN KEY (adventurer_id) REFERENCES adventurers (adventurer_id),
    CONSTRAINT fk_ag_guild      FOREIGN KEY (guild_id)      REFERENCES guilds      (guild_id)
) ENGINE=InnoDB;

CREATE TABLE quests (
    quest_id    INT          NOT NULL,
    title       VARCHAR(150) NOT NULL,
    difficulty  VARCHAR(50)  NOT NULL,
    reward_gold INT          NOT NULL,
    PRIMARY KEY (quest_id)
) ENGINE=InnoDB;

CREATE TABLE quest_completion (
    completion_id   INT  NOT NULL,
    adventurer_id   INT  NOT NULL,
    quest_id        INT  NOT NULL,
    completion_date DATE NOT NULL,
    score           INT  NOT NULL,
    PRIMARY KEY (completion_id),
    CONSTRAINT fk_qc_adventurer FOREIGN KEY (adventurer_id) REFERENCES adventurers    (adventurer_id),
    CONSTRAINT fk_qc_quest      FOREIGN KEY (quest_id)      REFERENCES quests         (quest_id)
) ENGINE=InnoDB;

CREATE TABLE skills (
    skill_id   INT          NOT NULL,
    skill_name VARCHAR(100) NOT NULL,
    category   VARCHAR(50)  NOT NULL,
    PRIMARY KEY (skill_id)
) ENGINE=InnoDB;

CREATE TABLE adventurer_skill (
    adventurer_id INT NOT NULL,
    skill_id      INT NOT NULL,
    mastery_level INT NOT NULL,
    PRIMARY KEY (adventurer_id, skill_id),
    CONSTRAINT fk_as_adventurer FOREIGN KEY (adventurer_id) REFERENCES adventurers (adventurer_id),
    CONSTRAINT fk_as_skill      FOREIGN KEY (skill_id)      REFERENCES skills      (skill_id)
) ENGINE=InnoDB;

-- =====================================================
-- ADVENTURERS (30 rows)
-- Classes: Chronomancer, Warrior, Mage, Rogue, Cleric, Ranger, Alchemist
-- Ranks: Novice, Apprentice, Adept, Expert, Master
-- =====================================================

INSERT INTO adventurers (adventurer_id, name, class, `rank`, `level`, join_date) VALUES
( 1, 'Aerin Shadowstep',    'Rogue',        'Master',     40, '2018-03-12'),
( 2, 'Bryndis Ironforge',   'Warrior',      'Expert',     35, '2019-07-04'),
( 3, 'Caelum Voss',         'Mage',         'Master',     42, '2017-11-21'),
( 4, 'Drusilla Nightwhisper','Cleric',      'Adept',      22, '2021-05-30'),
( 5, 'Eldrin Quickfingers', 'Rogue',        'Apprentice', 10, '2023-01-15'),
( 6, 'Fenris Bloodaxe',     'Warrior',      'Master',     45, '2016-08-09'),
( 7, 'Galatea Moonweave',   'Chronomancer', 'Expert',     38, '2019-02-18'),
( 8, 'Harwick Thornbush',   'Ranger',       'Adept',      25, '2020-10-05'),
( 9, 'Isolde Flamecaster',  'Mage',         'Expert',     33, '2020-04-22'),
(10, 'Jorvak the Stout',    'Warrior',      'Novice',      5, '2024-06-01'),
(11, 'Kessa Dawnbrew',      'Alchemist',    'Adept',      20, '2021-09-14'),
(12, 'Loran Spellbane',     'Mage',         'Apprentice', 12, '2022-12-03'),
(13, 'Mireth Coldspring',   'Cleric',       'Master',     44, '2015-06-27'),
(14, 'Nyx Emberthorn',      'Rogue',        'Expert',     36, '2018-11-11'),
(15, 'Oswald Greymantle',   'Chronomancer', 'Master',     47, '2014-03-08'),
(16, 'Priya Sunshard',      'Alchemist',    'Expert',     30, '2019-08-19'),
(17, 'Quelith Darkweave',   'Rogue',        'Adept',      21, '2021-04-07'),
(18, 'Riven Ashcloak',      'Ranger',       'Novice',      7, '2024-01-20'),
(19, 'Sylvara Frostbloom',  'Mage',         'Adept',      24, '2021-07-16'),
(20, 'Thane Goldbuckle',    'Warrior',      'Apprentice', 14, '2022-09-30'),
(21, 'Umara Windwhisper',   'Ranger',       'Expert',     31, '2019-05-25'),
(22, 'Valdris Nightbane',   'Chronomancer', 'Adept',      27, '2020-12-11'),
(23, 'Wella Stoneheart',    'Cleric',       'Apprentice', 11, '2023-03-04'),
(24, 'Xander Pyreblast',    'Mage',         'Novice',      6, '2024-02-28'),
(25, 'Ysolde Veinhook',     'Alchemist',    'Novice',      4, '2024-08-10'),
(26, 'Zephyr Crownfall',    'Warrior',      'Expert',     34, '2018-06-17'),
(27, 'Astra Hollowbark',    'Cleric',       'Master',     40, '2017-09-02'),
(28, 'Bram Copperveil',     'Alchemist',    'Apprentice', 13, '2022-11-22'),
(29, 'Corin Swiftarrow',    'Ranger',       'Master',     41, '2016-04-14'),
(30, 'Deva Mistwalker',     'Chronomancer', 'Novice',      8, '2023-10-09');

-- =====================================================
-- GUILDS (8 rows — some will have no adventurers)
-- =====================================================

INSERT INTO guilds (guild_id, guild_name, region) VALUES
(1, 'Iron Vanguard',       'Northern Reaches'),
(2, 'The Silver Compass',  'Coastal Expanse'),
(3, 'Ember Circle',        'Ashlands'),
(4, 'Thornwood Alliance',  'Midforest'),
(5, 'Celestial Accord',    'High Peaks'),
(6, 'The Hollow Blade',    'Eastern Wastes'),
(7, 'Dusk Covenant',       'Shadow Marches'),  -- no adventurers (practice RIGHT JOIN)
(8, 'Gilded Compass',      'Trade Heartlands'); -- no adventurers (practice RIGHT JOIN)

-- =====================================================
-- ADVENTURER_GUILD
-- Some adventurers belong to guilds, some do not.
-- Adventurers with NO guild: 5, 10, 18, 24, 25, 30
-- =====================================================

INSERT INTO adventurer_guild (adventurer_id, guild_id, joined_guild_date) VALUES
( 1, 1, '2018-04-01'),
( 2, 1, '2019-08-15'),
( 3, 2, '2018-01-10'),
( 4, 4, '2021-06-20'),
( 6, 1, '2016-09-01'),
( 7, 5, '2019-03-05'),
( 8, 4, '2020-11-12'),
( 9, 2, '2020-05-18'),
(11, 3, '2021-10-01'),
(12, 3, '2023-01-08'),
(13, 5, '2015-07-14'),
(14, 6, '2018-12-22'),
(15, 5, '2014-04-19'),
(16, 2, '2019-09-27'),
(17, 6, '2021-05-03'),
(19, 3, '2021-08-20'),
(20, 4, '2022-10-31'),
(21, 2, '2019-06-14'),
(22, 7, '2021-01-07'),   -- guild 7 will still have one member; guild 7 and 8 are "ghost" guilds for RIGHT JOIN
(23, 4, '2023-04-11'),
(26, 1, '2018-07-29'),
(27, 5, '2017-10-03'),
(28, 3, '2023-01-15'),
(29, 6, '2016-05-22');

-- NOTE: Adventurers 5, 10, 18, 24, 25, 30 have NO guild (good for LEFT JOIN practice)
-- NOTE: Guild 8 (Gilded Compass) has NO members (good for RIGHT JOIN practice)

-- =====================================================
-- QUESTS (15 rows)
-- Difficulties: Easy, Medium, Hard, Epic, Legendary
-- =====================================================

INSERT INTO quests (quest_id, title, difficulty, reward_gold) VALUES
( 1, 'Rat Cellar Clearance',          'Easy',      50),
( 2, 'Missing Merchant Caravan',      'Easy',     100),
( 3, 'Forest Bandit Camp',            'Medium',   250),
( 4, 'The Cursed Watermill',          'Medium',   300),
( 5, 'Escort to Ironhold Keep',       'Medium',   350),
( 6, 'Ruins of Ashenvale',            'Hard',     600),
( 7, 'The Bloodmoon Ritual',          'Hard',     750),
( 8, 'Siege of the Northern Gate',    'Hard',     800),
( 9, 'Dragon Egg Heist',              'Epic',    1500),
(10, 'Throne of the Lich King',       'Epic',    2000),
(11, 'Vault of the Forgotten Gods',   'Epic',    2500),
(12, 'Shatter the World Seal',        'Legendary',5000),
(13, 'The Last Chronolord',           'Legendary',6000),
(14, 'Abyssal Rift Closing',          'Legendary',7500),
(15, 'Goblin Market Supplies',        'Easy',      75);

-- =====================================================
-- QUEST_COMPLETION (40 rows)
-- Some adventurers have no completions: 5, 10, 18, 24, 25, 30, 20, 23, 28
-- =====================================================

INSERT INTO quest_completion (completion_id, adventurer_id, quest_id, completion_date, score) VALUES
( 1,  1,  3, '2018-09-14',  82),
( 2,  1,  6, '2019-05-20',  90),
( 3,  1,  9, '2020-11-03',  88),
( 4,  2,  1, '2019-09-01',  70),
( 5,  2,  4, '2020-03-17',  75),
( 6,  2,  8, '2021-06-22',  80),
( 7,  3,  7, '2018-07-30',  95),
( 8,  3, 10, '2019-12-14',  97),
( 9,  3, 12, '2021-03-08',  99),
(10,  4,  2, '2021-08-11',  60),
(11,  4,  5, '2022-01-25',  65),
( 12,  6,  8, '2017-04-19',  88),
(13,  6, 11, '2018-10-31',  91),
(14,  6, 13, '2020-07-15',  94),
(15,  7,  7, '2019-11-22',  85),
(16,  7, 13, '2021-05-09',  92),
(17,  8,  3, '2021-02-14',  73),
(18,  8,  5, '2021-12-01',  77),
(19,  9,  6, '2020-08-18',  84),
(20,  9, 10, '2021-09-27',  89),
(21, 11,  1, '2021-11-05',  55),
(22, 11,  4, '2022-06-14',  62),
(23, 12,  2, '2023-02-20',  58),
(24, 13,  9, '2016-04-03',  96),
(25, 13, 12, '2017-08-19',  98),
(26, 13, 14, '2019-01-31',  99),
(27, 14,  6, '2019-03-07',  87),
(28, 14,  9, '2020-10-22',  91),
(29, 15, 13, '2015-07-28',  97),
(30, 15, 14, '2016-11-12',  98),
(31, 16,  4, '2020-01-17',  72),
(32, 16,  5, '2020-09-25',  78),
(33, 17,  3, '2021-06-30',  68),
(34, 19,  2, '2021-10-08',  63),
(35, 21,  5, '2020-01-14',  76),
(36, 21,  8, '2020-12-19',  83),
(37, 22,  7, '2021-03-23',  80),
(38, 26,  8, '2019-02-11',  86),
(39, 27,  9, '2018-04-29',  93),
(40, 29, 11, '2017-06-15',  90);

-- =====================================================
-- SKILLS (15 rows — some unassigned to anyone)
-- Categories: Combat, Magic, Stealth, Support, Crafting
-- Unassigned skills: 13, 14, 15
-- =====================================================

INSERT INTO skills (skill_id, skill_name, category) VALUES
( 1, 'Backstab',            'Combat'),
( 2, 'Fireball',            'Magic'),
( 3, 'Ice Lance',           'Magic'),
( 4, 'Shadow Step',         'Stealth'),
( 5, 'Time Rewind',         'Magic'),
( 6, 'Holy Smite',          'Combat'),
( 7, 'Poison Brew',         'Crafting'),
( 8, 'Precise Shot',        'Combat'),
( 9, 'Shield Wall',         'Combat'),
(10, 'Heal Pulse',          'Support'),
(11, 'Camouflage',          'Stealth'),
(12, 'Transmutation',       'Crafting'),
(13, 'Aether Sight',        'Magic'),    -- unassigned
(14, 'Blood Pact',          'Support'),  -- unassigned
(15, 'Rune Carving',        'Crafting'); -- unassigned

-- =====================================================
-- ADVENTURER_SKILL (35 rows)
-- Some adventurers have no skills: 10, 18, 24, 25, 30
-- =====================================================

INSERT INTO adventurer_skill (adventurer_id, skill_id, mastery_level) VALUES
( 1,  1, 5),
( 1,  4, 4),
( 2,  9, 5),
( 3,  2, 5),
( 3,  3, 4),
( 4,  6, 3),
( 4, 10, 3),
( 5,  4, 1),
( 6,  9, 5),
( 7,  5, 5),
( 7,  3, 4),
( 8,  8, 4),
( 8, 11, 3),
( 9,  2, 4),
( 9,  3, 3),
(11,  7, 3),
(11, 12, 2),
(12,  2, 2),
(13,  6, 5),
(13, 10, 5),
(14,  1, 4),
(14,  4, 5),
(15,  5, 5),
(16,  7, 4),
(16, 12, 4),
(17,  1, 3),
(17, 11, 2),
(19,  2, 3),
(20,  9, 2),
(21,  8, 4),
(22,  5, 4),
(23, 10, 2),
(26,  9, 4),
(27,  6, 5),
(29,  8, 5);

-- =====================================================
-- END OF SETUP
-- =====================================================
