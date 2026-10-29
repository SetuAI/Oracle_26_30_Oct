"""
================================================================================
 CLAIM SETTLEMENT AGENT WITH A LIVE ADJUSTER
================================================================================

 THE PROBLEM
 -----------
 A motor insurance company receives thousands of claims a day. Two facts are in
 tension:

   - Most claims are small and obvious. Paying them by hand is slow and costly.
   - Some claims are large or suspicious. Paying those automatically is reckless.

 So the business question is not "can a machine settle claims?" It is:

        WHICH claims can be settled without a person,
        and for the rest, how does a person get involved
        without stopping the whole pipeline?

 WHAT WE ARE BUILDING
 --------------------
 A graph that investigates a claim, scores it, and then decides WHO decides.

   1. An AGENT gathers facts using tools (policy, claim history, garage quote).
      The LLM chooses which tools to call and how many times.

   2. PYTHON scores the claim. Not the LLM. The amount that leaves the bank is
      decided by arithmetic you can read, because a regulator will ask why.

   3. A ROUTER checks the score and the amount:
        small and clean   -> settle automatically, no human
        large or risky    -> PAUSE and ask a human adjuster

   4. The ADJUSTER can APPROVE, MODIFY the amount, or REJECT. Each answer sends
      the graph down a different path. The human is a branch, not a rubber stamp.

    START -> [investigate] <--+
                  |           | tool calls
                  v           |
               [tools] -------+
                  |  no more tool calls
                  v
              [assess]  score 
                  |
          +-------+--------+
      low risk          high risk or big payout
      small amount            |
          |                   v
          |            [human_review]   <-- graph PAUSES here
          |                   |
          |        +----------+----------+
          |     approve     modify     reject
          |        |          |          |
          v        v          v          v
     [auto_settle] [settle] [settle]   [deny]
          |             |               |
          +-------------+--------------+
                        v
                       END

================================================================================
"""