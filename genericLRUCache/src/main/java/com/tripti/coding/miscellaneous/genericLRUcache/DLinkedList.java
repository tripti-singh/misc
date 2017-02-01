package com.tripti.coding.miscellaneous.genericLRUcache;

/**
 * A Doubly Linked List
 * 
 * @author Tripti
 *
 */
public class DLinkedList<K, V> {
	CacheNode<K, V> head;
	CacheNode<K, V> tail;

	public DLinkedList() {
		head = null;
		tail = null;
	}

	public CacheNode<K, V> addNode(K key, V value) {
		CacheNode<K, V> node = new CacheNode<K, V>(key, value, null, null);
		if (head == null) {
			head = node;
			tail = node;
		} else {
			tail.next = node;
			node.prev = tail;
			tail = node;
		}
		return node;
	}

	public void moveToLast(CacheNode<K, V> node) {
		if (head == null) {
			head = node;
			tail = node;
		}
		if (head == tail || tail == node) {
			// Single node or node already last, do nothing
			System.out.println("Node was already most recently used");
			return;
		} else {
			if (node == head) {
				head = node.next;
			} else {
				node.prev.next = node.next;
			}
			node.next.prev = node.prev;
			node.next = null;
			node.prev = tail;
			tail.next = node;
			tail = node;

		}
	}

	public K removeLRU() {
		if (head == null) {
			return null;
		}
		K key = head.getKey();
		head.next.prev = null;
		head = head.next;
		return key;
	}

	public void printList() {
		CacheNode<K, V> oneNode = head;
		System.out.print("Printing List:");
		while (oneNode != null) {
			System.out.print(oneNode.getKey() + ": " + oneNode.getValue() + " --> ");
			oneNode = oneNode.next;
		}
		System.out.println("");
	}
}
