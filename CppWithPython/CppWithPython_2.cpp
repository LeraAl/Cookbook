// CppWithPython_2.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <fstream>
#include <iostream>
#include <map>

using namespace std;

int main()
{
	ifstream fin("input.txt", ios_base::in);
	int x, y;
	multimap<int, int> myMap;
	if (fin.is_open())
	{
		cout << "OK\n";
	}
	while (!fin.eof())
	{
		fin >> x >> y;
		myMap.insert(pair<int, int> (x, y));
	}
	fin.close();

	bool flag = true;
	for (auto i = myMap.begin(); i != myMap.end(); i++)
	{
		for (auto j = i; j != myMap.end(); )
		{
			j++;
			if (j != myMap.end() && i->first == j->first && i->second > j->second) {
				int temp = i->second;
				i->second = j->second;
				j->second = temp;
			}
		}
	}

	ofstream fout("output.txt", ios_base::out);

	/*for (auto i = myMap.begin(); i != myMap.end(); i++)
	{
		fout << i->first << ' ' << i->second << endl;
		cout << i->first << ' ' << i->second << endl;
	}*/

	for (int i = -11; i <= 10; i++) {
		fout << i << ' ' << i*i << endl;
	}
	fout.close();

	system("python.exe python.py");

	cin >> x;
    return 0;
}

