package com.tripti.coding.miscellaneous.genericLRUcache;

import java.io.IOException;
import java.util.Scanner;

/**
 * Hello world!
 *
 */
public class CacheUser {
	public static void main(String[] args) throws IOException {
		Scanner sc = new Scanner(System.in);
		try {
			System.out.println("Hello World!");
			LRUCache<String, String> myCache = new LRUCache<String, String>(3);
			while (true) {
				String key = sc.next();
				if (key.equals("exit")) {
					sc.close();
					break;
				}
				String value = myCache.getValue(key);
				System.out.println("APP:: " + key + " is: " + value);
			}
		} finally {
			sc.close();
		}
	}
}
