# 2024-Spring-HW2

Please complete the report problem below:

## Problem 1
Provide your profitable path, the amountIn, amountOut value for each swap, and your final reward (your tokenB balance).

> path: tokenB->tokenA->tokenD->tokenC->tokenB
swap from tokenB to tokenA: amountIn = 5, amountOut = 5.655321988655322
swap from tokenA to tokenD: amountIn = 5.655321988655322, amountOut = 2.458781317097934
swap from tokenD to tokenC: amountIn = 2.458781317097934, amountOut = 5.088927293301516
swap from tokenC to tokenB: amountIn = 5.088927293301516, amountOut = 20.129888944077447
tokenB balance = 20.129888944077447

## Problem 2
What is slippage in AMM, and how does Uniswap V2 address this issue? Please illustrate with a function as an example.

> Slippage is the difference between the expected price for a trade and the price you actually get when the trade is executed. This happens because the price fluctuates between the time you submit your trade and when it's actually processed on the blockchain.

Uniswap V2 addresses slippage by allowing the users to specify a minimum output amount that they are willing to accept. If the price changes beyond the minimum, the transaction will simply revert. For example, in the function 'swapTokensForExactTokens', we can see that users can limit the slippage by setting 'amountOutMin' to a suitable value. 

'''
function swapExactTokensForTokens(
    uint256 amountIn,
    uint256 amountOutMin,
    address[] calldata path,
    address to,
    uint256 deadline
) external returns (uint256[] memory amounts);
'''

## Problem 3
Please examine the mint function in the UniswapV2Pair contract. Upon initial liquidity minting, a minimum liquidity is subtracted. What is the rationale behind this design?

> By burning a small amount of liquidity, it ensures that there's always a tiny part of the pool that is not owned by anyone, preventing any liquidity provider from gaining complete control over the pool. It also prevents the case where the liquidity becomes (close to) zero, which would potentially cause division by zero errors or rounding errors.

## Problem 4
Investigate the minting function in the UniswapV2Pair contract. When depositing tokens (not for the first time), liquidity can only be obtained using a specific formula. What is the intention behind this?

> When providers deposit tokens into an existing liquidity pool, the liquidity provider receives an amount of liquidity determined by a specific formula. The formula is designed to ensure that the new liquidity is proportional to the provider's share of the total liquidity pool. The formula also maintains the ratio between the tokens, which prevents arbitragers from intentionally interfering with the price of the tokens in the pool by adding liquidity.

## Problem 5
What is a sandwich attack, and how might it impact you when initiating a swap?

> If an attacker identifies a pending transaction from a user to buy in a token that has not yet been confirmed, the attacker can initiate their own transaction before the user's transaction (by raising the gas price). The attacker's transaction increases the price of token, which causes the user buying in at a higher price and receiving less token, while the attacker benefits from the the price difference caused by the user's transaction.

