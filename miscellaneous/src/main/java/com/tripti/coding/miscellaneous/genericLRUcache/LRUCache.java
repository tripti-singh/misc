package com.tripti.coding.miscellaneous.genericLRUcache;

import java.util.HashMap;
import java.util.Map;

public class LRUCache<K,V> {
	private Map<K,CacheNode<K,V>> keyCache;
	private DLinkedList<K,V> lruList;
	private int cacheSize;
	
	public LRUCache(int cacheSize) {
		keyCache = new HashMap<K, CacheNode<K,V>>();
		lruList = new DLinkedList<K,V>();
		this.cacheSize = cacheSize;
	}
	public V getValue(K key){
		V value=null;
		if(keyCache.containsKey(key)){
			System.out.println("Cache Hit!!!");
			CacheNode<K,V> node = keyCache.get(key); 
			value = node.getValue();
			//Move to end of list
			lruList.moveToLast(node);
		} else {
			System.out.println("Cache Miss. generating new value...");
			value = (V) ("Value"+(Math.ceil(Math.random()*100)));
			setValueInCache(key,value);
		}
		lruList.printList();
		return value;
	}
	
	private void setValueInCache(K key, V value){
		if(keyCache.size()>=cacheSize){
			K removeKey = lruList.removeLRU();
			keyCache.remove(removeKey);
			System.out.println("Cache Full.... removing "+removeKey);
		}
		CacheNode<K,V> node = lruList.addNode(key, value);
		keyCache.put(key, node);
	}
}