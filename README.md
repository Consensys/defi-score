[![All Contributors](https://img.shields.io/badge/all_contributors-4-orange.svg?style=flat-square)](#contributors)
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

* #### Smart Contract Security (35%)
  Errors, bugs and unexpected outcomes in smart contracts can cause real financial harm. These risks can be minimized by proactive code audits and formal verification from reputable security firms.

  Our model assesses code security by looking at three pieces of off-chain but public data:

  1. **Audited Code:** Has the code been audited by a reputable security team?
  2. **Formal Verification:** Has the code been formally verified by a reputable security team?
  3. **Bounty Program:** Does the development team offers a public bug bounty program?

* #### Smart Contract Openness (15%)
  Part of the promise of DeFi is that the functionality of smart contracts is completely on-chain, which means they are verifiable and transparent. Developers of DeFi platforms still have the ability to obscure their code in various ways, such as not verifying the bytecode and using off chain oracles processes. Security through obscurity offers weak security guarantees at best, and at worst results in delays in finding critical bugs.

### II. Financial Risk

* #### Collateral (25%)
  Part of the promise of DeFi is that the functionality of smart contracts is completely on-chain, which means they are verifiable and transparent. Developers of DeFi platforms still have the ability to obscure their code in various ways, such as not verifying the bytecode and using off chain oracles processes. Security through obscurity offers weak security guarantees at best, and at worst results in delays in finding critical bugs.

* #### Liquidity (10%)
  The currently scoped platforms all attempt to incentive liquidity by using dynamic interest rate models which produce varying rates depending on the level of liquidity in each asset pool. However, incentivized liquidity does not mean guaranteed liquidity. The absolute level of liquidity is used instead of the percentage utilization (outstandingDebt/totalAssets) because it has a side effect of also scoring larger pools higher.

### III. Other Considerations

* #### Insurance/Regulatory Risk (15%)
  While there are some promising innovations in the DeFi insurance space, none are widespread or mature enough yet. Also, none of these platforms’ development teams are actually decentralized yet and none have been approved by the United States or other nations’ banking/finance regulatory bodies yet.


## Further Reading:
[DeFi Score: Assessing Risk in Permissionless Lending Protocols](whitepaper.md)



## Contributors
<!-- ALL-CONTRIBUTORS-LIST:START - Do not remove or modify this section -->
<!-- prettier-ignore-start -->
<!-- markdownlint-disable -->
<table>
  <tr>
    <td align="center"><a href="https://github.com/jclancy93"><img src="https://avatars2.githubusercontent.com/u/7850202?v=4" width="100px;" alt="Jack Clancy"/><br /><sub><b>Jack Clancy</b></sub></a><br /><a href="https://github.com/ConsenSys/defi-score/commits?author=jclancy93" title="Code">💻</a> <a href="https://github.com/ConsenSys/defi-score/commits?author=jclancy93" title="Documentation">📖</a> <a href="#talk-jclancy93" title="Talks">📢</a></td>
    <td align="center"><a href="https://twitter.com/JordanLyall"><img src="https://avatars0.githubusercontent.com/u/999289?v=4" width="100px;" alt="Jordan Lyall"/><br /><sub><b>Jordan Lyall</b></sub></a><br /><a href="#projectManagement-jordanlyall" title="Project Management">📆</a> <a href="https://github.com/ConsenSys/defi-score/commits?author=jordanlyall" title="Documentation">📖</a> <a href="#design-jordanlyall" title="Design">🎨</a></td>
    <td align="center"><a href="https://github.com/flamingYawn"><img src="https://avatars3.githubusercontent.com/u/11626601?v=4" width="100px;" alt="tlip"/><br /><sub><b>tlip</b></sub></a><br /><a href="#design-flamingYawn" title="Design">🎨</a> <a href="#content-flamingYawn" title="Content">🖋</a></td>
    <td align="center"><a href="https://github.com/ispytodd"><img src="https://avatars2.githubusercontent.com/u/29828992?v=4" width="100px;" alt="ispytodd"/><br /><sub><b>ispytodd</b></sub></a><br /><a href="#content-ispytodd" title="Content">🖋</a> <a href="#blog-ispytodd" title="Blogposts">📝</a></td>
  </tr>
</table>

<!-- markdownlint-enable -->
<!-- prettier-ignore-end -->
<!-- ALL-CONTRIBUTORS-LIST:END -->

## Community
Join the DeFi Score community on [Telegram](https://t.me/defiscore).

## License
<a rel="license" href="http://creativecommons.org/licenses/by-sa/2.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by-sa/2.0/80x15.png" /></a><br />This work is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by-sa/2.0/">Creative Commons Attribution-ShareAlike 2.0 Generic License</a>.
