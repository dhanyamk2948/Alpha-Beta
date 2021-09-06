# Alpha-Beta
This contains an interactive way to analyse the performance of a stock if we know the alpha and beta values of a particular stock.

Well, although there are numerous parameters and methods to analyse the performance of a particular stock, but one of the easy and logical way to do that is with the help of alpha and beta values of a stock.
So what are these alpha and beta values? What do these values convey?

## Alpha:
It is the excess return on an investment after adjusting for market-related volatility and random fluctuations.

## Beta:
Beta is a measure of volatility relative to a benchmark, such as the S&P 500. 
<br>


</br>
Great definitions!!! But what do these mean? How do we make sense of them?

Here's how------------
                                           
                                          beta>1
                                           |
                                           |
                  high beta                |            high beta 
                  low alpha                |            high alpha
                                           |                
                      (2nd)                |                (1st)
                                           |
                                           |
                                    (beta=1|alpha=0)
      alpha<0------------------------------|------------------------------alpha>0
                                           |
                                           |
                   low beta                |            low beta
                   Low alpha               |            high alpha
                                           |
                       (3rd)               |                 (4th)
                                           |
                                           |
                                           |
                                        beta<1   
                                        
So , it alpha and beta values fall in any of these quadrants , what can we conclude from that?

1st quadrant- Although the returns are high, the volitality is high too, these kind of stocks rewuire what is called active trading based on momentum strategy.

2nd quadrant- Here alpha is low i.e. returns will be lower than market but volitality will be very high, these stocks are best for day-trading.

3rd quadrant- These are low return low volitality stocks, ideally we wont profit much from these but they can give profits in the form of dividends.

4th quadrant- This is the ideal quadrant for long-term investment, where there is minimal risk and highest returns, suitable for passive traders.

Now, what the code does is, takes in values of alpha and beta and analyses the stock based on the quadrant that it falls in.

An example of how this would look:
![image](https://user-images.githubusercontent.com/69901065/132213434-3540a931-346d-405f-a843-d6aab658fa8a.png)

That's all for now, THANKS:)


Suggestions for improvement are welcome.
