package com.tripti.coding.miscellaneous.genericLRUcache;

public class CacheNode<K, V> {
	private K key;
	private V value;

	public K getKey() {
		return key;
	}

	public V getValue() {
		return value;
	}

	CacheNode<K, V> prev;
	CacheNode<K, V> next;

	public CacheNode(K key, V value, CacheNode<K, V> prev, CacheNode<K, V> next) {
		this.key = key;
		this.value = value;
		this.prev = prev;
		this.next = next;
	}
}