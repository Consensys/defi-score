<img src="assets/images/banner.png" alt="DeFi Score">

# DeFi Score
> A framework for assessing risk in permissionless lending platforms.

DeFi Score is a single, consistently comparable value for measuring protocol risk, based on factors including smart contract risk, collateralization, and liquidity.

We encourage the Ethereum community to evolve the methodology, making it more effective and easier to use.

Join the discussion on [Telegram](https://t.me/defiscore).

## Overview
Four loko freegan seitan butcher tote bag. Fixie master cleanse microdosing fam typewriter. Pug photo booth yr jean shorts subway tile, whatever artisan lumbersexual intelligentsia flannel mlkshk flexitarian.

### The Components
What factors into a protocol’s DeFi Score?

| Smart Contract Risk  | Financial Risk | Other Considerations |
|----------------------|---------------------------------|----------------------|
| Audited Code         | Collateral Makeup CVaR          | Insurance Risk       |
| Byte Source Verified | Collateralization Ratio 30d EMA | Regulatory Risk      |
| Formal Verification  | Liquidity 30d EMA               |                      |
| Bug Bounty Program   |                                 |                      |


### Example
Four loko freegan seitan butcher tote bag. Fixie master cleanse microdosing fam typewriter. Pug photo booth yr jean shorts subway tile, whatever artisan lumbersexual intelligentsia flannel mlkshk flexitarian.

> Insert example

## Table of Contents
> insert ToC

## Introduction
Below we introduce a model for assessing risk levels in various permissionless lending protocols. To account for the variety of risks present in these platforms, we use a multi-factor model that looks at smart contract, collateral, and liquidity risks. The model uses a mix of public off-chain and on-chain data to best estimate the relative levels of risk across multiple different permissionless, Ethereum-based lending products.

### Motivation
A major impetus for Satoshi Nakamoto in creating Bitcoin was the 2008 financial crisis. The genesis block of Bitcoin contained a reference to the bank bailouts of that time. Some felt that the crisis precipitating these bailouts was caused in part by the legacy financial world’s misunderstanding and mispricing of credit risk throughout the financial system.

In the last year, we have seen an explosion of smart contract based financial protocols, many catering to the lending and borrowing markets. These markets have grown into the largest sub-category of so-called “decentralized finance” or “DeFi” and experienced 355% YoY growth. However, not all lending platforms are created equal. Different lending products have very different risk/reward profiles, which makes comparing their rates alone akin to comparing apples to oranges.

Better understanding and modelling of risk in the DeFi space would be an important step towards maturity. There is much work to be done, but now is the time to start. Hopefully this model and others like it can begin to lay the groundwork for robust risk evaluation in DeFi.

### DeFi Protocols
[ Can we just provide a short paragraph explaining these DeFi protocols -- i.e., they are based on smart contracts, which are just code that is run on the ethereum blockchain (maybe mention consensus), and typically include a user “locking” collateral in the protocol in exchange for some return. ]

## Components

### Smart Contract Risk
Smart Contract Risk is the main contributor to counterparty risk in DeFi. While DeFi is often referred to as trustless, a user of a DeFi platform must trust the smart contract they are interacting with. A smart contract could be opaque to a user, which means a user is trusting the contract code in the same way a user trusts any web 2.0 infrastructure. There is also the risk that a smart contract is hacked because it is insecure, which has grave financial implications for any and all users of the hacked protocol, including, for example, loss of all collateral locked in the protocol. Our proposed model looks at two elements of smart contract risk.

#### Code Security
The security of smart contracts are extremely important when evaluating the risk of users losing funds that are stored in a smart contract when interacting with many DeFi platforms. As the ecosystem has learned, errors in smart contracts can result in significant financial damage. For example, the so-called “DAO hack” was an attack launched against a project commonly referred to as “The DAO,” which was an early example of a Decentralized Autonomous Organization ‐‐ i.e., a “virtual” organization embodied in smart contracts on the Ethereum blockchain. On June 17, 2016, an unknown individual or group began rapidly diverting ETH from The DAO, causing approximately 3.6 million ETH—1/3 of The DAO’s total ETH—to move from The DAO’s Ethereum Blockchain address to an Ethereum Blockchain address controlled by the attacker.

While no smart contract can be guaranteed as safe and free of bugs, a thorough code audit and formal verification process from a reputable security firm helps uncover critical, high severity bugs that otherwise could result in financial harm to users. Bug bounty programs are another positive indicator that the development team takes security seriously by incentivizing independent security researchers to discover protocol bugs, ultimately allowing for a more widespread security review.

Our model assesses code security by looking at three pieces of off-chain but public data:

1. Audited Code: The first is whether the code been audited by a reputable security team (Consensys Diligence, Trail of Bits, others??).
2. Formal Verification:The second data point is whether the code has been formally verified by a reputable security team.
3. Bounty Program:The third data point is whether the development team offers a public bug bounty program.

#### Code Openness
Part of the promise of DeFi is that the functionality of smart contracts is completely on-chain, which means they are verifiable and transparent. Developers of DeFi platforms still have the ability to obscure their code in various ways, such as not verifying the bytecode and using off chain oracles processes. Security through obscurity offers weak security guarantees at best, and at worst results in delays in finding critical bugs. While bytecode decompilation is possible, it is a difficult and time-consuming process and makes it hard to follow the mantra of “don’t trust, verify”.

Code openness is assessed by looking at a single data point of off-chain but public data, whether the byte code has been verified.

### Financial Risk
DeFi contains many of the same risks as legacy finance. While most lending platforms use over-collateralization to reduce credit risk, over-collateralization does not completely remove credit risk. Crypto assets are notoriously volatile and these platforms have no method to recover from system insolvency caused by volatile collateral assets.

The current model looks at two elements of financial risk:

#### Collateral
Without a widely accepted approach to on-chain reputation or identity, the only method to avoid unwanted amounts of credit risk in DeFi money market platforms is to use over-collateralization. While all of the current platforms use very conservative collateral factors, the highly volatile nature of crypto assets means that these high collateral factors may still be insufficient.

The makeup of collateral assets that back these DeFi platforms also have a high level of variation, with some being made up of much more liquid, stable assets than others. For example, a platform may be primarily backed by ETH. While ETH is still a very volatile asset, it is relatively stable and liquid compared to an asset like LINK. These collateral makeup differences are an important factor when thinking about platform risk.

Collateral Risk is assessed by looking at two pieces of data, both derivable from on-chain data. The first data point is the 30 day Exponential Moving Average (EMA) of the collateralization ratio, which is normalized using logarithmic min-max normalization across all of the available lending pools.  The second data point is an analysis of the collateral portfolio. Generally, EMA is calculated as follows:

[insert EMA formula graphic]

Where:

* The coefficient α represents the degree of weighting decrease, a constant smoothing factor between 0 and 1. A smoothing factor of 2/31 has been chosen.
* Yt is the value at a time period t. This is 30 for finding a 30d EMA
* St is the value of the EMA at any time period t.

[insert histogram]

There are many different models to assess the risk of a portfolio of assets. One of the most common models is the VaR (Value at Risk) model. There are multiple different variations of the VaR model. This model currently uses the CVaR (Conditional Value at Risk) model, also known as the Expected Shortfall model. The methodology uses CVaR over VaR because CVaR better captures the probability and drawdown of more extreme scenarios. The above figure helps demonstrate this difference-- the CVAR (ES) model results in a larger potential drawdown. Due to the nascency and extreme volatility present in crypto assets, the methodology is more conservative. The model uses the 99% CVaR model with the following formula:

[insert formula]

The complement of the percentage is taken as a higher CVAR is worse because it means that a higher percentage of the total Collateral is at risk.


#### Liquidity
The currently scoped platforms all attempt to incentive liquidity by using dynamic interest rate models which produce varying rates depending on the level of liquidity in each asset pool. However, incentivized liquidity does not mean guaranteed liquidity. A user takes on risk that they will not be able to withdraw their lent out assets on demand because all the assets are currently lent out.

Liquidity risk is assessed by a single data point that is derivable from on-chain data, which is the level of liquidity. This data point is the 30 day EMA of liquidity, normalized using logarithmic min-max normalization of the amount of liquidity in USD across all of the available lending pools. The absolute level of liquidity is used instead of the percentage utilization (outstandingDebt/totalAssets) because it has a side effect of also scoring larger pools higher.


### Other Considerations

#### Insurance
In most developed banking systems, money market accounts have some form of deposit insurance. In the US, this deposit insurance is FDIC insurance, which insures a single bank deposit account up to $250,000. There is no equivalent deposit insurance in the DeFi ecosystem yet. While there are some promising innovations in the DeFi insurance space (Nexus Mutual), none are widespread or mature enough yet.

Some platforms are contributing a portion of the interest accrued on their platform to an insurance reserve, in case of a liquidity squeeze or black swan event. However, these insurance pools are nowhere near large enough to cover a large insolvency event on one of these platforms.


#### Regulatory Risk
DeFi as an industry is extremely nascent. Algorithmic money markets are even more so. None of these platforms’ development teams are actually decentralized yet and none have been approved by the United States or other nations’ banking/finance regulatory bodies yet. This means that the user of these platforms also takes on some level of regulatory risk when interacting with them.

## Formula

1. Smart Contract Risk (50%)
* Audited code (25%)
* All code’s byte source verified (15%)
* Formal Verification (5%)
* Bug Bounty Program (5%)

2. Financial Risk (35%)
* Collateral Makeup CVaR (10%)
* Collateralization Ratio 30d EMA (15%)
* Liquidity 30d EMA (10%)

3. Other Considerations (15%)
* Insurance/Regulatory Risk

## Limitations
This is not a validated statistical model. There is not enough data to properly validate this model on a product wide basis. This is an opinion based estimation framework to estimate the risks associated with different DeFI platforms.

This rating methodology is based on the opinions of the investment quality on a relatively short term basis (less than one year). These recommendations are also not indicative of the size of the investment, which may have a material impact on the level of liquidity risk. This methodology is in an early stage and any users of this rating system should expect frequent updates.

This methodology attempts to compare different DeFi money market platforms on a relative basis, not on an absolute basis. This is a comparison between other DeFi money market platforms and legacy financial investments, like deposit accounts. The DeFi space is extremely nascent, and without a wealth of historical data, it is more difficult to make forward-looking statements.

__This model does not consider many other risks that are relevant to these products, such as oracle risk, centralization risks and liquidation policies.__


## Future Improvements
There is much work still to do on this model. This is early stage research. This model needs more fine-tuning and validation. There is also a need to include other relevant risks in this model, like centralization risks, oracle risks and liquidation policy risks. Some of these are hard to quantify, which is why they were not included in the initial iteration.

Eventually, it might also make sense to break some of these scoring sub components down into their own, more robust scoring algorithms. This way the subcomponents can be composed to score different types of blockchain finance products. Future coverage could include additional DeFi earning products like Set, synthetic asset products like Maker and UMA, market making products like Uniswap and the various CeFI counterparts of these products.

Another eventual goal is to provide an API for this and other scoring algorithms that other first and second layer DeFi products would be able to leverage. This will allow for improved user education and outcomes in the space.

This methodology will be initially open sourced on Github, but the eventual goal is to make the model more community managed by allowing for decentralized governance to determine factor weighting and factor inclusion.

The eventual goal of this research is to converge all of the work done into a sort of risk DAO, that could act like an open source credit rating agency that would determine methodologies and provide grant funding to engineers, risk management experts and others that contribute to this living body of work. While the amount of risk management work that needs to be done in the space is daunting, we are excited about the future.


## Contributors
> Insert 3box profiles of Contributors

## Key Contributors:
* Jack Clancy

## Additional Contributors:
* Jordan Lyall
* Todd Murtha
* Thomas Lipari
* [and the rest]

## Community
Join the DeFi Score community on [Telegram](https://t.me/defiscore).

## Used By
> Stay tuned

## License
<a rel="license" href="http://creativecommons.org/licenses/by-sa/2.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by-sa/2.0/80x15.png" /></a><br />This work is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by-sa/2.0/">Creative Commons Attribution-ShareAlike 2.0 Generic License</a>.
