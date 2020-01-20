### Problem Statement

Protocols are consistently adding support for new assets. How should we decide when to list those assets and start assigning scores to them? Listing low liquidity assets will result in a shift to the score so we will want to be thoughtful about supporting new pools

### Proposal
Pool support should happen when the pool liquidity and or total supply is stable at or above $10,000 for one week. It seems overbearing to enforce formal verification of these figures for the time being. The method to verify if a pool has sustained these levels is a simple manual check on Loanscan or a similar alternative.

### Alternatives
1. Support pools as soon as they are listed (no threshold)

   Listing all pools would require more engineering resources and would also have a side effect of affecting the scores more drastically, which is non-ideal.
	 

2. Higher pool support thresholds (~100,000)

   This would limit user choice and would not allow us to list new assets as fast as other sites.


3. Automated checking or code enabled checking

   This is a viable alternative but there might not always be a programmatic way to fetch new assets from the chain or an api. It would also likely require a custom solution per protocol we support. It makes sense to revisit this at a later date and build this system ad hoc.
