import 'package:flutter/material.dart';



class RegisterDemo extends StatelessWidget {
  const RegisterDemo({super.key});

  final _sizeTextBlack = const TextStyle(fontSize: 20.0, color: Colors.black);
  final _sizeTextWhite = const TextStyle(fontSize: 20.0, color: Colors.white);

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      debugShowCheckedModeBanner: false,
      home: Scaffold(
        body: Center(
          child: Column(
            mainAxisAlignment: MainAxisAlignment.center,
            children: <Widget>[
              Container(
                child: TextFormField(
                  decoration: InputDecoration(labelText: "Email:"),
                  keyboardType: TextInputType.emailAddress,
                  style: _sizeTextBlack,
                ),
                width: 400.0,
              ),
              Container(
                child: TextFormField(
                  decoration: InputDecoration(labelText: "Password:"),
                  obscureText: true,
                  style: _sizeTextBlack,
                ),
                width: 400.0,
                padding: EdgeInsets.only(top: 10.0),
              ),
              Container(
                child: TextFormField(
                  decoration: InputDecoration(labelText: "Repeat password:"),
                  obscureText: true,
                  style: _sizeTextBlack,
                ),
                width: 400.0,
                padding: EdgeInsets.only(top: 10.0),
              ),
              Container(
                child: TextFormField(
                  decoration: InputDecoration(labelText: "Phone number:"),
                  obscureText: false,
                  style: _sizeTextBlack,
                ),
                width: 400.0,
                padding: EdgeInsets.only(top: 10.0),
              ),
              Padding(
                padding: EdgeInsets.only(top: 25.0),
                child: MaterialButton(
                  onPressed: () {
                    Navigator.of(context).push(
                      MaterialPageRoute(
                        builder: (BuildContext context) {
                          return const Scaffold();
                        },
                      ),
                    );
                  },
                  color: Color.fromARGB(255, 158, 79, 170),
                  height: 50.0,
                  minWidth: 150.0,
                  child: Text(
                    "Register",
                    style: _sizeTextWhite,
                  ),
                ),
              )
            ],
          ),
        ),
      ),
    );
  }
}