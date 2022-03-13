s.boot;

~g1 = Group.new();

~g2 = Group.after(~g1);

~g3 = Group.head(~g2);

~g4 = Group.before(~g3);


~g1.nodeID;
~g2.nodeID;
~g3.nodeID;
~g4.nodeID;