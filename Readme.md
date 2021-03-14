# Readme

Quickly hacked together code formatter for apex.
Feel free to adapt it to your needs.

This project is a work in progress solution and can change any time.

## Installation

1. move the `apex-formatter.py` file to some location you like. I have mine on `~/.apex-formatter.py`.

1. You may need to perform a `chmod +x apex-formatter.py` in order for it to be executable.

1. install https://marketplace.visualstudio.com/items?itemName=jkillian.custom-local-formatters
and set the apex-formatter.py as formatter for apex in the settings.json:
(find the settings.json by Cmd+Shift+P -> settings -> Extensions -> Custom Local Formatter -> Emmet -> "Extension path" )

    ```json
    "customLocalFormatters.formatters": [
        {
        "command": "python c://Users/PathToFormatter/apex-formatter.py",
        "languages": ["apex"]
        }
    ],
    ```

## Example

### Before
```java
public class MyDummyClass{
    public String hello='I am a teststring';

    public void testMethod(){
                 Integer a=5;
  if(a>=14){
            System.debug('This is a debug meessage');
        }
// Comment are ignored a+b=c. still indent though!
List<B>b=new List<B>{new B(),new B()};
        Integer manySpaces=  a*  3;
    
    B b2= new B(
        Name='myName'  ,
Age=14
  )
    

    }




        }

```

### After

```java
public class MyDummyClass{
    public String hello = 'I am a teststring';
    
    public void testMethod(){
        Integer a = 5;
        if(a >= 14){
            System.debug('This is a debug meessage');
        }
        // Comment are ignored a+b=c. still indent though!
        List<B> b = new List<B> { new B(), new B() };
        Integer manySpaces = a * 3;
        
        B b2 = new B(
            Name = 'myName',
            Age = 14
        )
        
    }
    
}
```

## TODO

- Allow to put {,(,[ always on new line
- No empty line over lines containing only: '}', ')' ');' '),' etc
    
### TO IGNORE:
- Content inside strings (quick: if ' " ' in line)
