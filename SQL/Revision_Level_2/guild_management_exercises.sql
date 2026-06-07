-- =====================================================
-- SQL PRACTICE - GUILD MANAGEMENT DB
-- 

-- Topics:
-- SELECT
-- WHERE
-- DISTINCT
-- LIKE
-- BETWEEN
-- IN
-- ORDER BY
-- LIMIT
-- OFFSET
-- MIN
-- MAX
-- AVG
-- GROUP BY
-- HAVING
-- CASE
-- YEAR
-- CURYEAR
-- INNER JOIN
-- LEFT JOIN
-- RIGHT JOIN
-- FULL JOIN simulation with UNION
-- CROSS JOIN
-- Multi-table JOIN
-- 

-- Database:
-- guild_management_db
-- 

-- Files used:
-- 1. guild_management_db.sql
--    Responsible for creating the database structure
--    and populating the tables.
-- 

-- 2. guild_management_exercises.sql
--    Used to practice SQL queries based on the guild database.
-- 

-- Main Tables:
-- adventurers
-- guilds
-- adventurer_guild
-- quests
-- quest_completion
-- skills
-- adventurer_skill
-- 

-- Goal:
-- Practice SQL data retrieval and analytics using a relational RPG guild database.
-- The focus is to understand filtering, aggregation, calculated columns,
-- and especially how to use different types of JOINs correctly.

-- IMPORTANT NOTE:
-- The columns `rank` and `level` in the adventurers table are MySQL reserved words.
-- Always wrap them in backticks when writing queries:
--   SELECT `rank`, `level` FROM adventurers;
--   ORDER BY `level` DESC;
--   WHERE `rank` = 'Master';
-- 

-- =====================================================

USE guild_management_db;

-- =====================================================
-- SECTION 1 — SINGLE TABLE REVIEW
-- Topics: SELECT, WHERE, DISTINCT, LIKE, BETWEEN,
--         IN, ORDER BY, LIMIT, OFFSET
-- =====================================================

-- Exercise 1
-- Retrieve the name, class, and level of all adventurers.
-- Sort the results by level in descending order.
-- Show the highest-level adventurers first.
SELECT
	name, class, level
FROM adventurers
ORDER BY level DESC;


-- Exercise 2
-- Find all adventurers whose rank is 'Master' or 'Expert'.
-- Use the IN operator.
-- Show only their name, class, and rank.
SELECT
	name, class, `rank`
FROM adventurers
WHERE `rank` IN ('Master', 'Expert');

-- Exercise 3
-- List all adventurers whose name starts with the letter 'A'.
-- Use LIKE.
-- Show name and class.
SELECT
	name, class
FROM adventurers
WHERE name LIKE 'A%';

-- Exercise 4
-- Find all adventurers whose level is between 20 and 40 (inclusive).
-- Use BETWEEN.
-- Show name, level, and rank.
-- Order by level ascending.
SELECT
	name, level, `rank`
FROM adventurers
WHERE `level` BETWEEN 20 AND 40
ORDER BY `level`;

-- Exercise 5
-- Return a list of all unique classes that appear in the adventurers table.
-- Use DISTINCT.
-- Order alphabetically.
SELECT 
	DISTINCT class 
FROM adventurers 
ORDER BY class;

-- Exercise 6
-- Find all quests with a reward_gold value greater than 500.
-- Show the title, difficulty, and reward_gold.
-- Order by reward_gold descending.
SELECT
	title, difficulty, reward_gold
FROM quests
WHERE reward_gold > 500
ORDER BY reward_gold DESC;

-- Exercise 7
-- Show the 5 adventurers with the lowest level.
-- Use ORDER BY and LIMIT.
-- Show name, class, and level.
SELECT 
	name, class, level
FROM adventurers
ORDER BY level
LIMIT 5;

-- Exercise 8
-- List adventurers who joined before January 1, 2020.
-- Use a WHERE condition on join_date.
-- Show name, class, and join_date.
-- Order by join_date ascending.
-- Skip the first 3 results using OFFSET.
-- Hint: OFFSET is used together with LIMIT.
SELECT 
	name, class, join_date
FROM adventurers
WHERE join_date < '2020-01-01'
ORDER BY join_date
LIMIT 10
OFFSET 3;

-- =====================================================
-- SECTION 2 — SUMMARY ANALYTICS
-- Topics: COUNT, MIN, MAX, AVG, GROUP BY, HAVING
-- =====================================================

-- Exercise 9
-- Count how many adventurers belong to each class.
-- Show class and the count.
-- Order by count descending.
SELECT
	class,
    COUNT(name) AS adventure_count
FROM adventurers
GROUP BY class
ORDER BY adventure_count DESC;

-- Exercise 10
-- Find the minimum, maximum, and average level for each rank.
-- Show rank, min_level, max_level, and avg_level.
-- Round avg_level to 1 decimal place.
-- Hint: Use ROUND().
SELECT
	`rank`,
    MIN(`level`) AS min_level,
    MAX(`level`) AS max_level,
    ROUND(AVG(`level`), 1) AS avg_level
FROM adventurers
GROUP BY `rank`;

-- Exercise 11
-- Find the total reward_gold available for each quest difficulty.
-- Show difficulty and total_gold.
-- Order by total_gold descending.
SELECT
	difficulty,
    SUM(reward_gold) AS total_gold
FROM quests
GROUP BY difficulty
ORDER BY total_gold DESC;

-- Exercise 12
-- Count how many quests each adventurer has completed.
-- Show adventurer_id and quest_count.
-- Only include adventurers who have completed MORE than 2 quests.
-- Use HAVING.
-- Order by quest_count descending.
SELECT
	adventurer_id,
    COUNT(quest_id) AS quest_count
FROM quest_completion
GROUP BY adventurer_id
HAVING quest_count > 2
ORDER BY quest_count DESC;

-- Exercise 13
-- Find the average score per adventurer in quest_completion.
-- Show adventurer_id and avg_score.
-- Only include adventurers with an average score of 80 or higher.
-- Round to 1 decimal place.
SELECT
	adventurer_id,
    ROUND(AVG(score), 1) AS avg_score
FROM quest_completion
GROUP BY adventurer_id
HAVING avg_score >= 80
ORDER BY avg_score DESC;

-- Exercise 14
-- How many skills exist in each category?
-- Show category and skill_count.
-- Only show categories with more than 2 skills.
-- Order by skill_count descending.

SELECT 
	category,
    COUNT(skill_name) AS skill_count
FROM skills
GROUP BY category
HAVING skill_count > 2
ORDER BY skill_count DESC;

-- =====================================================
-- SECTION 3 — CALCULATED COLUMNS
-- Topics: CASE, IF, YEAR, CURDATE, derived columns
-- =====================================================

-- Exercise 15
-- Add a calculated column called 'experience_tier' based on level:
--   Level 1-10:  'Beginner'
--   Level 11-25: 'Intermediate'
--   Level 26-39: 'Advanced'
--   Level 40+:   'Legendary'
-- Use CASE WHEN.
-- Show name, level, and experience_tier.
-- Order by level descending.
SELECT
	name,
    level,
    CASE
		WHEN `level` >= 1 AND `level` <= 10 THEN 'Beginner'
        WHEN `level` >= 11 AND `level` <= 25 THEN 'Intermediate'
        WHEN `level` >= 26 AND `level` <= 39 THEN 'Advanced'
        WHEN `level` >= 40 THEN 'Legendary'
    END AS experience_tier
FROM adventurers
ORDER BY `level` DESC;

-- Exercise 16
-- Add a column called 'gold_category' to the quests table:
--   reward_gold < 200:   'Low Reward'
--   reward_gold 200-999: 'Standard Reward'
--   reward_gold >= 1000: 'High Reward'
-- Use CASE WHEN.
-- Show title, reward_gold, and gold_category.
SELECT
	title,
    reward_gold,
    CASE
		WHEN reward_gold < 200 THEN 'Low Reward'
        WHEN reward_gold >= 200 AND reward_gold <= 999 THEN 'Standard Reward'
        WHEN reward_gold >= 1000 THEN 'High Reward'
    END AS gold_category
FROM quests
ORDER BY reward_gold DESC;

-- Exercise 17
-- Show each adventurer's name and the year they joined, using the YEAR() function.
-- Also add a column called 'years_active' that calculates how many years
-- they have been with the guild (from join_date to today).
-- Hint: Use YEAR(CURDATE()) - YEAR(join_date).
SELECT
	name,
    YEAR(join_date) AS joined_year,
    (YEAR(CURDATE()) - YEAR(join_date)) AS years_active
FROM adventurers
ORDER BY years_active DESC;

-- Exercise 18
-- In quest_completion, add a column called 'performance' using IF():
--   score >= 85: 'High Performer'
--   score < 85:  'Needs Improvement'
-- Show completion_id, adventurer_id, score, and performance.
SELECT
	completion_id,
    adventurer_id,
    score,
    IF(score >= 85, 'High Performer', 'Needs Improvement') AS performance
FROM quest_completion
ORDER BY performance DESC;

-- Exercise 19
-- Calculate a 'bonus_gold' column for each quest:
--   Epic and Legendary quests get a 20% bonus added to reward_gold.
--   All other quests get no bonus (show reward_gold as is).
-- Use CASE WHEN to compute the bonus.
-- Show title, difficulty, reward_gold, and bonus_gold.
-- Hint: You can do arithmetic inside CASE.
SELECT
	title,
    difficulty,
    reward_gold,
    CASE
		WHEN difficulty = 'Epic' OR difficulty = 'Legendary' THEN ROUND(1.2*reward_gold, 0)
        ELSE reward_gold
    END AS bonus_gold
FROM quests
ORDER BY difficulty DESC;

-- =====================================================
-- SECTION 4 — JOIN FUNDAMENTALS
-- Topics: INNER JOIN, LEFT JOIN, RIGHT JOIN,
--         identifying unmatched records, choosing JOIN type
-- =====================================================

-- Exercise 20
-- Retrieve the name and class of every adventurer
-- along with the name of the guild they belong to.
-- Only show adventurers who ARE in a guild.
-- Hint: You need to join adventurers → adventurer_guild → guilds.
--       Think about which JOIN type returns only matched rows.
SELECT * FROM adventurers;
SELECT * FROM adventurer_guild;

SELECT
	a.name,
    a.class,
    g.guild_name
FROM adventurers a
INNER JOIN adventurer_guild ag
ON a.adventurer_id = ag.adventurer_id
INNER JOIN guilds g
ON ag.guild_id = g.guild_id;

-- Exercise 21
-- List ALL adventurers and show their guild name if they have one.
-- If an adventurer does not belong to any guild, show NULL for guild_name.
-- Hint: This requires a LEFT JOIN from adventurers outward.
-- Show name, class, and guild_name.
SELECT
	a.name,
    a.class,
    g.guild_name
FROM adventurers a
LEFT JOIN adventurer_guild ag
ON a.adventurer_id = ag.adventurer_id
LEFT JOIN guilds g
ON g.guild_id = ag.guild_id;

-- Exercise 22
-- Find all adventurers who do NOT belong to any guild.
-- Use a LEFT JOIN and filter for NULL on the right side.
-- Show name and class.
-- Hint: After a LEFT JOIN, unmatched rows have NULL in the joined table's columns.
SELECT
	name,
    class
FROM adventurers a
LEFT JOIN adventurer_guild ag
ON a.adventurer_id = ag.adventurer_id
WHERE ag.guild_id IS NULL;

-- Exercise 23
-- List all guilds and show the adventurers who belong to each.
-- Guilds with no adventurers should still appear, with NULL for adventurer details.
-- Hint: Think about which table should be on the LEFT side of the join.
-- Show guild_name, region, and adventurer name.
	SELECT
		g.guild_name,
		g.region,
		a.name AS adventurers
	FROM guilds g
	LEFT JOIN adventurer_guild ag
	ON g.guild_id = ag.guild_id
	LEFT JOIN adventurers a
	ON a.adventurer_id = ag.adventurer_id;

-- Exercise 24
-- Find all guilds that currently have NO adventurers registered.
-- Use a RIGHT JOIN (or LEFT JOIN from guilds) and filter for NULLs.
-- Show guild_name and region.
SELECT
	g.guild_name,
    g.region
FROM guilds g
LEFT JOIN adventurer_guild ag
ON g.guild_id = ag.guild_id
WHERE ag.adventurer_id IS NULL;

-- Exercise 25
-- Retrieve all quest completions along with the adventurer's name
-- and the quest title.
-- Only show completions where both the adventurer and quest exist (matched rows only).
-- Show adventurer name, quest title, completion_date, and score.
SELECT
	a.name AS adventurer_name,
    q.title AS quest_title,
    qc.completion_date,
    qc.score
FROM quest_completion qc
INNER JOIN adventurers a
ON qc.adventurer_id = a.adventurer_id
INNER JOIN quests q
ON qc.quest_id = q.quest_id;

-- Exercise 26
-- List all skills and show which adventurers have learned each skill.
-- Skills that no adventurer has learned should still appear in the results.
-- Show skill_name, category, and adventurer name (NULL if no one has learned it).
-- Hint: RIGHT JOIN from adventurer_skill → skills, or LEFT JOIN from skills outward.
SELECT
	s.skill_name,
    s.category,
    a.name AS adventurer_name
FROM skills s
LEFT JOIN adventurer_skill ads
ON s.skill_id = ads.skill_id
LEFT JOIN adventurers a
ON ads.adventurer_id = a.adventurer_id;

-- Exercise 27
-- Find all skills that have NOT been assigned to any adventurer.
-- Use an appropriate JOIN and filter for NULLs.
-- Show skill_name and category.
SELECT
	s.skill_name,
    s.category
FROM adventurer_skill ads
RIGHT JOIN skills s
ON ads.skill_id = s.skill_id
WHERE ads.adventurer_id IS NULL;

-- Exercise 28
-- Show every adventurer alongside their completed quest titles.
-- Include adventurers who have NEVER completed any quest (show NULL for quest info).
-- Show name, class, and quest title.
-- Hint: LEFT JOIN adventurers to quest_completion, then join to quests.
SELECT
	a.name AS adventurer_name,
    a.class,
    GROUP_CONCAT(q.title SEPARATOR " - ") AS quests_title
FROM adventurers a
LEFT JOIN quest_completion qc
ON a.adventurer_id = qc.adventurer_id
LEFT JOIN quests q
ON qc.quest_id = q.quest_id
GROUP BY a.name, a.class;

-- Exercise 29
-- In the adventurer_guild table, some adventurers joined guilds after 2020.
-- List those adventurers' names, their guild name, and the date they joined the guild.
-- Use INNER JOIN and filter by joined_guild_date.
SELECT
	a.name AS adventurer_name,
    g.guild_name,
    ag.joined_guild_date
FROM adventurer_guild ag
INNER JOIN adventurers a
ON ag.adventurer_id = a.adventurer_id
INNER JOIN guilds g
ON ag.guild_id = g.guild_id
WHERE YEAR(ag.joined_guild_date) >= 2020
ORDER BY ag.joined_guild_date;

-- =====================================================
-- SECTION 5 — ADVANCED JOIN PRACTICE
-- Topics: Multi-table JOIN, GROUP BY after JOIN,
--         HAVING after JOIN, CROSS JOIN,
--         FULL JOIN simulation with UNION, GROUP_CONCAT
-- =====================================================

-- Exercise 30
-- For each guild, count how many adventurers it has.
-- Use JOIN + GROUP BY.
-- Show guild_name, region, and member_count.
-- Include guilds with 0 members.
-- Order by member_count descending.
-- Hint: A LEFT JOIN from guilds to adventurer_guild will include guilds with no members.
--       COUNT(adventurer_id) counts only non-NULL values.
SELECT
	g.guild_name,
    g.region,
    COUNT(a.adventurer_id) AS member_count
FROM guilds g
LEFT JOIN adventurer_guild ag
ON g.guild_id = ag.guild_id
LEFT JOIN adventurers a
ON ag.adventurer_id = a.adventurer_id
GROUP BY g.guild_name, g.region
ORDER BY member_count DESC;

-- Exercise 31
-- Find all guilds that have MORE than 3 adventurers.
-- Use JOIN + GROUP BY + HAVING.
-- Show guild_name and member_count.
SELECT
	g.guild_name,
    COUNT(a.adventurer_id) AS member_count
FROM guilds g
LEFT JOIN adventurer_guild ag
ON g.guild_id = ag.guild_id
LEFT JOIN adventurers a
ON ag.adventurer_id = a.adventurer_id
GROUP BY g.guild_name
HAVING member_count > 3
ORDER BY member_count DESC;

-- Exercise 32
-- For each adventurer who has completed quests, calculate:
--   - Their total number of completions
--   - Their average score
--   - Their highest score
-- Show name, total_completions, avg_score (rounded to 1 decimal), and best_score.
-- Only include adventurers with at least 2 completions.
-- Order by avg_score descending.
SELECT
	a.name AS adventurer_name,
    COUNT(qc.completion_id) AS total_completion,
    ROUND(AVG(qc.score),1) AS avg_score,
    MAX(qc.score) AS best_score
FROM quest_completion qc
INNER JOIN quests q
ON qc.quest_id = q.quest_id
INNER JOIN adventurers a
ON qc.adventurer_id = a.adventurer_id
GROUP BY a.name
HAVING total_completion >= 2
ORDER BY avg_score DESC;

-- Exercise 33
-- List each guild with the names of all its members concatenated into one string.
-- Use GROUP_CONCAT to combine member names.
-- Show guild_name and a column called 'members' with names separated by ', '.
-- Hint: GROUP_CONCAT(column ORDER BY column SEPARATOR ', ')
-- Only include guilds that have at least one member.
SELECT
	g.guild_name,
    GROUP_CONCAT(a.name SEPARATOR ", ") AS members
FROM guilds g
INNER JOIN adventurer_guild ag
ON g.guild_id = ag.guild_id
INNER JOIN adventurers a
ON ag.adventurer_id = a.adventurer_id
GROUP BY g.guild_name;

-- Exercise 34
-- Simulate a FULL OUTER JOIN between adventurers and guilds
-- to see every adventurer AND every guild, regardless of whether they are linked.
-- Use a UNION of LEFT JOIN and RIGHT JOIN.
-- Show adventurer name (or NULL) and guild_name (or NULL).
-- Hint:
--   Part 1: LEFT JOIN adventurers to adventurer_guild to guilds
--   Part 2: RIGHT JOIN adventurers to adventurer_guild to guilds
--   UNION removes duplicates.
SELECT
	a.name AS adventurer_name,
    g.guild_name
FROM adventurers a
LEFT JOIN adventurer_guild ag
ON a.adventurer_id = ag.adventurer_id
LEFT JOIN guilds g
ON ag.guild_id = g.guild_id
UNION
SELECT
	a.name AS adventurer_name,
    g.guild_name
FROM adventurers a
RIGHT JOIN adventurer_guild ag
ON a.adventurer_id = ag.adventurer_id
RIGHT JOIN guilds g
ON ag.guild_id = g.guild_id;

# Not redundant answer
-- Part 1:All adventurers (with and without guild)
SELECT
    a.name AS adventurer_name,
    g.guild_name
FROM adventurers a
LEFT JOIN adventurer_guild ag
    ON a.adventurer_id = ag.adventurer_id
LEFT JOIN guilds g
    ON ag.guild_id = g.guild_id

UNION

-- Part 2: Only guilds that has no adventure
SELECT
    NULL AS adventurer_name,
    g.guild_name
FROM guilds g
LEFT JOIN adventurer_guild ag
    ON g.guild_id = ag.guild_id
WHERE ag.adventurer_id IS NULL;

-- Exercise 35
-- Produce a CROSS JOIN between quest difficulties and adventurer ranks.
-- This creates every possible combination of difficulty and rank.
-- Show difficulty and rank as two columns.
-- Hint: Use two subqueries or DISTINCT selections from the relevant tables.
--       CROSS JOIN produces M x N rows (no ON condition needed).
SELECT 
	q.difficulty,
    a.`rank`
FROM quests q
CROSS JOIN adventurers a;

-- Exercise 36
-- For each region, list all adventurers in that region along with
-- the total number of quests they have completed.
-- Include adventurers with 0 completions.
-- Show region, adventurer name, and quest_count.
-- Order by region, then by quest_count descending.
-- Hint: You will need to join guilds → adventurer_guild → adventurers → quest_completion.
SELECT
	g.region,
    a.name AS adventurer_name,
    COUNT(qc.quest_id) AS quest_count
FROM guilds g
LEFT JOIN adventurer_guild ag
ON g.guild_id = ag.guild_id
LEFT JOIN adventurers a
ON ag.adventurer_id = a.adventurer_id
LEFT JOIN quest_completion qc
ON qc.adventurer_id = a.adventurer_id
GROUP BY g.region, a.name
ORDER BY g.region, quest_count DESC;

-- Exercise 37
-- Find adventurers who have mastered at least one skill at mastery_level 5
-- AND have completed at least one quest with a score above 90.
-- Show adventurer name, class, and rank.
-- Hint: You may need to join multiple tables and use HAVING or subqueries with EXISTS / IN.
SELECT DISTINCT
	a.name AS adventurer_name,
    a.class,
    a.`rank`
FROM adventurers a
INNER JOIN adventurer_skill ads
ON a.adventurer_id = ads.adventurer_id
INNER JOIN quest_completion qc
ON a.adventurer_id = qc.adventurer_id
WHERE ads.mastery_level = 5 AND qc.score > 90;

-- =====================================================
-- SECTION 6 — BOSS FIGHT
-- Combined: Multi-table JOIN, aggregation, CASE,
--           ORDER BY, LIMIT, HAVING
-- =====================================================

-- Exercise 38
-- BOSS FIGHT 1: Guild Performance Report
-- -----------------------------------------
-- Produce a report showing, for each guild:
--   - guild_name
--   - region
--   - member_count (number of adventurers)
--   - avg_level (average adventurer level, rounded to 1 decimal)
--   - total_quest_completions (sum of all quest completions by all members)
--   - guild_tier: classify each guild using CASE:
--       total_quest_completions >= 10 → 'Elite'
--       total_quest_completions 5-9   → 'Active'
--       total_quest_completions < 5   → 'Developing'
--       (handle guilds with 0 completions as 'Developing')
-- Include only guilds with at least 1 member.
-- Order by total_quest_completions descending.
-- Hint: You will need to join guilds, adventurer_guild, adventurers, and quest_completion.
--       Use LEFT JOINs carefully so adventurers without completions are still counted.
--       GROUP BY guild.
SELECT
	g.guild_name,
    g.region,
	COUNT(DISTINCT a.adventurer_id) AS member_count,
    ROUND(AVG(a.`level`), 1) AS avg_level,
    COUNT(qc.completion_id) AS total_quest_completions,
    CASE
		WHEN COUNT(qc.completion_id) >= 10 THEN 'Elite'
        WHEN COUNT(qc.completion_id) >= 5 THEN 'Active'
        ELSE 'Developing'
    END AS guild_tiar
    FROM guilds g
    LEFT JOIN adventurer_guild ag
    ON g.guild_id = ag.guild_id
    LEFT JOIN adventurers a
    ON ag.adventurer_id = a.adventurer_id
    LEFT JOIN quest_completion qc
    ON a.adventurer_id = qc.adventurer_id
    GROUP BY g.guild_name, g.region
    ORDER BY total_quest_completions DESC;

-- Exercise 39
-- BOSS FIGHT 2: Top Performing Adventurers Leaderboard
-- -------------------------------------------------------
-- Rank adventurers by overall performance using this formula:
--   performance_score = (avg_score * 0.5) + (total_completions * 10) + (level * 2)
-- Show:
--   - adventurer name
--   - class
--   - rank
--   - guild_name (NULL if no guild)
--   - total_completions
--   - avg_score (rounded to 1 decimal)
--   - performance_score (rounded to 1 decimal)
-- Only include adventurers who have completed at least 1 quest.
-- Order by performance_score descending.
-- Limit to the top 10.
-- Hint: You need to join adventurers, quest_completion, and optionally adventurer_guild + guilds.
--       Calculate the derived column in SELECT using arithmetic.
SELECT
    a.name AS adventurer_name,
    a.class,
    a.`rank`,
    g.guild_name,
    COUNT(qc.completion_id) AS total_completions,
    ROUND(AVG(qc.score), 1) AS avg_score,
    ROUND((ROUND(AVG(qc.score), 1) * 0.5) + (COUNT(qc.completion_id) * 10) + (a.`level` * 2), 1) AS performance_score
FROM adventurers a
LEFT JOIN adventurer_guild ag
    ON a.adventurer_id = ag.adventurer_id
LEFT JOIN guilds g
    ON ag.guild_id = g.guild_id
LEFT JOIN quest_completion qc
    ON a.adventurer_id = qc.adventurer_id
WHERE qc.completion_id IS NOT NULL
GROUP BY a.adventurer_id, a.name, a.class, a.`rank`, a.`level`, g.guild_name
ORDER BY performance_score DESC
LIMIT 10;

-- Exercise 40
-- BOSS FIGHT 3: Quest Difficulty Breakdown by Class
-- ---------------------------------------------------
-- For each combination of adventurer class and quest difficulty:
--   - Count how many quest completions occurred (completion_count)
--   - Calculate the average score (avg_score, rounded to 1 decimal)
--   - Add a label called 'result_quality':
--       avg_score >= 90 → 'Outstanding'
--       avg_score >= 75 → 'Solid'
--       avg_score < 75  → 'Needs Work'
-- Only include combinations with at least 2 completions.
-- Order by class, then by avg_score descending.
-- Hint: Join adventurers → quest_completion → quests.
--       GROUP BY two columns: class and difficulty.
--       HAVING filters on aggregate values.
--       CASE can reference the alias only in ORDER BY, not HAVING — use the expression again.
SELECT
	a.class,
    q.difficulty,
	COUNT(qc.completion_id) AS completion_count,
    ROUND(AVG(qc.score),1) AS avg_score,
    CASE
		WHEN ROUND(AVG(qc.score),1) >= 90 THEN 'Outstanding'
        WHEN ROUND(AVG(qc.score),1) >= 75 THEN 'Solid'
        ELSE 'Needs Work'
    END AS result_quality
FROM adventurers a
LEFT JOIN quest_completion qc
ON a.adventurer_id = qc.adventurer_id
LEFT JOIN quests q
ON qc.quest_id = q.quest_id
GROUP BY a.class, q.difficulty
HAVING completion_count >= 2
ORDER BY a.class, avg_score DESC;

-- =====================================================
-- END OF EXERCISES
-- =====================================================
