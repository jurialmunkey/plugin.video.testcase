Test case plugin to reproduce reuselanguageinvoker widget crash.

See diff below for Estuary testcase.


```diff
diff --git a/xml/Home.xml b/xml/Home.xml
index 4192e93..38d7ecf 100644
--- a/xml/Home.xml
+++ b/xml/Home.xml
@@ -43,6 +43,28 @@
 					<effect type="slide" end="0,20" time="180" tween="sine" delay="80" />
 				</animation>
 				<include>OpenClose_Right</include>
+				<control type="group" id="18000">
+					<visible>String.IsEqual(Container(9000).ListItem.Property(id),testcase)</visible>
+					<include content="Visible_Right_Delayed">
+						<param name="id" value="testcase"/>
+					</include>
+					<control type="grouplist" id="18001">
+						<include>WidgetGroupListCommon</include>
+						<pagecontrol>18010</pagecontrol>
+						<include content="WidgetListPoster">
+							<param name="content_path" value="plugin://plugin.video.testcase/?info=list01&amp;reload=$INFO[Window(Home).Property(reload)]"/>
+							<param name="widget_header" value="TEST1"/>
+							<param name="widget_target" value="videos"/>
+							<param name="list_id" value="18100"/>
+						</include>
+						<include content="WidgetListPoster">
+							<param name="content_path" value="plugin://plugin.video.testcase/?info=list02&amp;reload=$INFO[Window(Home).Property(reload)]"/>
+							<param name="widget_header" value="TEST2"/>
+							<param name="widget_target" value="videos"/>
+							<param name="list_id" value="18200"/>
+						</include>
+					</control>
+				</control>
 				<control type="group" id="5000">
 					<visible>String.IsEqual(Container(9000).ListItem.Property(id),movies)</visible>
 					<include content="Visible_Right_Delayed">
@@ -902,6 +924,12 @@
 						</control>
 					</itemlayout>
 					<content>
+						<item>
+							<label>TestCase</label>
+							<onclick>ActivateWindow(Videos,plugin://plugin.video.testcase/,return)</onclick>
+							<property name="menu_id">$NUMBER[18000]</property>
+							<property name="id">testcase</property>
+						</item>
 						<item>
 							<label>$LOCALIZE[342]</label>
 							<onclick condition="Library.HasContent(movies) + Skin.HasSetting(home_no_categories_widget)">ActivateWindow(Videos,videodb://movies/,return)</onclick>
```