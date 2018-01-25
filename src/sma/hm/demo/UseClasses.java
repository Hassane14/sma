package sma.hm.demo;

import java.util.Arrays;

import sma.hm.classes.*;
import sma.hm.classes.Class;
import sma.hm.classes.impl.*;

public class UseClasses {
	public static void main (String[] args) {
		System.out.println("Demonstration of how the classes can be used in Java:\n");
		
		System.out.println("Creating a Class `node`");
		ClassesFactoryImpl factory = new ClassesFactoryImpl();
		Class node = factory.createClass();
		node.setName("node");
		
		System.out.println("Creating two attributes `id` and `desc`");
		Attribute nodeId = factory.createAttribute();
		nodeId.setCls(node);
		nodeId.setName("id");
		nodeId.setType(Type.INTEGER);
		node.set_primary_key(nodeId);
		
		Attribute nodeName = factory.createAttribute();
		nodeName.setCls(node);
		nodeName.setName("desc");
		nodeName.setType(Type.STRING);
		
		System.out.print("Now node's attributes are: ");
		System.out.println(Arrays.deepToString(node.getAttributes().toArray()));
		
		System.out.print("Node's primary key is: ");
		System.out.println(node.get_primary_key());
		
		System.out.println("Creating a reference `parent`");
		Reference parent = factory.createReference();
		parent.setCls(node);
		parent.setTarget(node);
		parent.setName("parent");
		
		System.out.print("Now node's references are: ");
		System.out.println(Arrays.deepToString(node.getReferences().toArray()));
		
		assert node.getReferences().get(0).getTarget() == node;
		System.out.println("OK.");
	}
}