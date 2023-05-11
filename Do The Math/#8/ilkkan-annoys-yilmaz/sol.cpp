#include <bits/stdc++.h>
using namespace std;

double sqr(double x) { return x * x; }

struct Point {
    double x, y;
    void read() {
        cin >> x >> y;
    }

    Point operator+(const Point &other) const {
        return Point({x + other.x, y + other.y});
    }

    Point operator-(const Point &other) const {
        return Point({x - other.x, y - other.y});
    }

    Point operator*(double factor) const {
        return Point({x * factor, y * factor});
    }

    Point operator/(double factor) const {
        return Point({x / factor, y / factor});
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
    int alpha;
    cin >> alpha;

    const double pi = atan(1) * 4;

    Point segment_center = (ilkkan + ersoy) / 2; // Linet segment that connects the glasses of İlkkan and Ersoy
    double segment_half_length = segment_center.distance(ilkkan);
    double circle_radius = segment_half_length / sin(alpha * pi / 180);
    double segment_center_to_circle_center_dist = circle_radius * cos(alpha * pi / 180);
    double factor = segment_center_to_circle_center_dist / segment_half_length;
    Point vector = segment_center - ilkkan;
    vector = Point({-vector.y, vector.x});
    Point circle_centers[] = {segment_center + vector * factor, segment_center - vector * factor};
    double dists[] = {yilmaz.distance(circle_centers[0]), yilmaz.distance(circle_centers[1])};
    double ans = min(abs(dists[0] - circle_radius), abs(dists[1] - circle_radius));
    cout << fixed << setprecision(4) << ans << "\n";
}