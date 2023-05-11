#include <bits/stdc++.h>
using namespace std;

double sqr(double x) { return x * x; }

struct Point {
    double x, y;
    void read() {
        cin >> x >> y;
    }

    Point center(const Point &other) const {
        return Point({(x + other.x) / 2, (y + other.y) / 2});
    }

    double distance(const Point &other) const {
        return sqrt(sqr(x - other.x) + sqr(y - other.y));
    }
};

int main() {
    Point ilkkan, yilmaz, ersoy;
    ilkkan.read();
    yilmaz.read();
    ersoy.read();

    Point center = yilmaz.center(ersoy);
    double radius = center.distance(ersoy);

    cout << fixed << setprecision(4) << abs(radius - center.distance(ilkkan)) << "\n";
}