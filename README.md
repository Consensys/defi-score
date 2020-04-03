[![All Contributors](https://img.shields.io/badge/all_contributors-6-orange.svg?style=flat-square)](#contributors)
<img src="assets/images/banner.png" alt="DeFi Score Banner">

The DeFi Score is a framework for assessing risk in permissionless lending platforms. It's a single, consistently comparable value for measuring protocol risk, based on factors including smart contract risk, collateralization, and liquidity.

We encourage the Ethereum community to evolve the methodology, making it more effective and easier to use.

* See live scores at [defiscore.io](https://defiscore.io).
* Read the detailed [whitepaper](whitepaper.md).
* Join the discussion on [Telegram](https://t.me/defiscore).

## Table of Contents
* [Example Scores](#example-scores)
* [Implementation](#implementation)
* [Components](#components)
* [Further Reading](#further-reading)
* [Contributors](#contributors)

## Example Scores
We've provided a few example scores with a breakdown of each component. Although the underlying methodology is complex, it should be simple for a user to understand.

<img src="assets/images/defiscore-example.png" alt="DeFi Score Examples">

## Implementation
Want to run the numbers yourself? Check out the [implementation instructions](implementation).

## Components
The DeFi Score methodology can be organized into Smart Contract Risk, Financial Risk, and Other Considerations.

<img src="assets/images/defiscore-components.png" alt="DeFi Score Banner Components">

### I. Smart Contract Risk

* #### Smart Contract Security (45%)
  Errors, bugs and unexpected outcomes in smart contracts can cause real financial harm. These risks can be minimized by proactive code audits and formal verification from reputable security firms.

  Our model assesses code security by looking at three pieces of off-chain but public data:

  1. **Time on Mainnet** Normalized time since the protocol first launched on mainnet
  2. **No Critical Vulnerabilities:** No vulnerabilities have been exploited
  3. **Four Engineer Weeks** 4 or more engineer weeks have been dedicated to auditing the protocol
  4. **Public Audit:** Has the audit report been made public
  5. **Recent Audit:** Has there been an audit in the last 12 months **OR** have no code changes been made
  6. **Bounty Program:** Does the development team offers a public bug bounty program?

### II. Financial Risk

* #### Collateral (20%)
  While all of the current platforms use very conservative collateral factors, the highly volatile nature of crypto assets means that these high collateral factors may still be insufficient. Collateral Risk is assessed by looking at two pieces of data, both derivable from on-chain data. The first data point is the utilization rate. The second data point is an analysis of the collateral portfolio using the CVaR (Conditional Value at Risk) model, also known as the Expected Shortfall model.

* #### Liquidity (10%)
  The currently scoped platforms all attempt to incentive liquidity by using dynamic interest rate models which produce varying rates depending on the level of liquidity in each asset pool. However, incentivized liquidity does not mean guaranteed liquidity. The absolute level of liquidity is used. 

### III. Centralization Risk

* #### Protocol Administration (12.5%)

One of the biggest contributors to centralization risk in DeFi protocols is the use of admin keys. Admin keys allow protocol developers to change different parameters of their smart contract systems like oracles, interest rates and potentially more. Protocol developer’s’ ability to alter these contract parameters allows them to cause financial loss to users. Measures like timelocks and multi-signature wallets help mitigate the risk of financial loss due to centralized elements. Mult-signature wallets help mitigate this risk by distributing control to a larger number of developers, meaning that the loss or compromise of a single private key cannot compromise the entire system. Timelocks help mitigate risk by allowing protocol users to exit their positions before a change can take place.

* #### Oracles (12.5%)

Another large element of centralization risk in these protocols is oracle centralization. There are many different flavors of oracle systems being used to power these protocols. Some protocols use a fully self-operated oracle system while others use externally operated oracles like Uniswap and Kyber. [Samczsun’s writeup](https://samczsun.com/taking-undercollateralized-loans-for-fun-and-for-profit/) on oracles and their ability to cause financial loss provides good background information. The oracle centralization score is not focused on whether these price feeds are manipulatable or not (they all are), but whether a single entity can manipulate them with ease. In the self-operated model, it only takes the oracle owner to manipulate its data. Decentralized oracles can’t be manipulated in the same way, but may not always represent the fair market value for an asset, which is why developers building on top of decentralized oracles opt to use price volatility bounds to defend against these types of attacks.


### Disclaimer

The current DeFi Score algorithm uses min max normalization for certain metrics (Utilization Index and Liquidity Index). Anyone can fork the code and add support for new pools. However, if you add a pool that introduces a new lower or upper bound of utilization or liquidity, this will have a material effect on the scores for all other pools. The DeFi score team regularly adds support for new pools once they meet our requirements which you can read more about [here](https://github.com/ConsenSys/defi-score/blob/master/pool-support-threshold.md).

## Further Reading:
[DeFi Score: Assessing Risk in Permissionless Lending Protocols](whitepaper.md)



## Contributors
<!-- ALL-CONTRIBUTORS-LIST:START - Do not remove or modify this section -->
<!-- prettier-ignore-start -->
<!-- markdownlint-disable -->
<table>
  <tr>
    <td align="center"><a href="https://github.com/jclancy93"><img src="https://avatars2.githubusercontent.com/u/7850202?v=4" width="100px;" alt=""/><br /><sub><b>Jack Clancy</b></sub></a><br /><a href="https://github.com/ConsenSys/defi-score/commits?author=jclancy93" title="Code">💻</a> <a href="https://github.com/ConsenSys/defi-score/commits?author=jclancy93" title="Documentation">📖</a> <a href="#talk-jclancy93" title="Talks">📢</a></td>
    <td align="center"><a href="https://twitter.com/JordanLyall"><img src="https://avatars0.githubusercontent.com/u/999289?v=4" width="100px;" alt=""/><br /><sub><b>Jordan Lyall</b></sub></a><br /><a href="#projectManagement-jordanlyall" title="Project Management">📆</a> <a href="https://github.com/ConsenSys/defi-score/commits?author=jordanlyall" title="Documentation">📖</a> <a href="#design-jordanlyall" title="Design">🎨</a></td>
    <td align="center"><a href="https://github.com/flamingYawn"><img src="https://avatars3.githubusercontent.com/u/11626601?v=4" width="100px;" alt=""/><br /><sub><b>tlip</b></sub></a><br /><a href="#design-flamingYawn" title="Design">🎨</a> <a href="#content-flamingYawn" title="Content">🖋</a></td>
    <td align="center"><a href="https://github.com/ispytodd"><img src="https://avatars2.githubusercontent.com/u/29828992?v=4" width="100px;" alt=""/><br /><sub><b>ispytodd</b></sub></a><br /><a href="#content-ispytodd" title="Content">🖋</a> <a href="#blog-ispytodd" title="Blogposts">📝</a></td>
    <td align="center"><a href="https://github.com/anthonyhuanggr"><img src="https://avatars0.githubusercontent.com/u/7041796?v=4" width="100px;" alt=""/><br /><sub><b>Anthony H.</b></sub></a><br /><a href="#translation-anthonyhuanggr" title="Translation">🌍</a></td>
    <td align="center"><a href="https://github.com/antonina-cherednichenko"><img src="https://avatars0.githubusercontent.com/u/1220854?v=4" width="100px;" alt=""/><br /><sub><b>Antonina Norair</b></sub></a><br /><a href="https://github.com/ConsenSys/defi-score/commits?author=antonina-cherednichenko" title="Documentation">📖</a></td>
    <td align="center"><a href="https://github.com/TomAFrench"><img src="https://avatars3.githubusercontent.com/u/15848336?v=4" width="100px;" alt=""/><br /><sub><b>Tom French</b></sub></a><br /><a href="https://github.com/ConsenSys/defi-score/commits?author=TomAFrench" title="Documentation">📖</a></td>
  </tr>
  <tr>
    <td align="center"><a href="https://github.com/karbica"><img src="https://avatars3.githubusercontent.com/u/8563742?v=4" width="100px;" alt=""/><br /><sub><b>Kevin Arbi</b></sub></a><br /><a href="https://github.com/ConsenSys/defi-score/commits?author=karbica" title="Code">💻</a></td>
  </tr>
</table>

<!-- markdownlint-enable -->
<!-- prettier-ignore-end -->
<!-- ALL-CONTRIBUTORS-LIST:END -->

## Community
Join the DeFi Score community on [Telegram](https://t.me/defiscore).

## License
<a rel="license" href="http://creativecommons.org/licenses/by-sa/2.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by-sa/2.0/80x15.png" /></a><br />This work is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by-sa/2.0/">Creative Commons Attribution-ShareAlike 2.0 Generic License</a>.
