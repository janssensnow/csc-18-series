Feature: Using the proxy design pattern to instantiate a huge object
         containing 10 million digits

         As a user I want to use the proxy design pattern to instantiate a huge object containing 10 million digits
         by starting a proxy, the object is counted and sorted. After counted the proxy is then deleted

         Scenario: A huge object will be instantiated
           Given I initialize proxy
           And proxy is started
           When the object is instantiated
           Then proxy counts then increments and sorts it