void main() {
  // factorization of a number
  // measure time

  var start = new DateTime.now();
  var n = 123456789;
  int i = 2;
  while (i <= n / 2 + 1) {
    if (n % i == 0) {
      print(i);
    }
    i = i + 1;
  }
  if (n > 1) {
    print(n);
  }

  var end = new DateTime.now();
  print('time = ${end.difference(start)}');
}
