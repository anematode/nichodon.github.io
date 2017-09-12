<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="1.0"
	xmlns:s="http://www.sitemaps.org/schemas/sitemap/0.9"
	xmlns:image="http://www.google.com/schemas/sitemap-image/1.1"
	xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
	<xsl:template match="/">
		<html>
			<head>
				<title>Sitemap</title>
				<link rel="stylesheet" type="text/css" href="styles.css" />
				<link rel="icon" href="images/favicon.png" sizes="16x16" type="image/png" />
				<meta name="viewport" content="width=device-width, initial-scale=1.0" />
			</head>
			<body>
				<div id="top"></div>
				<div class="content">
					<div class="article">
						<h1>Sitemap</h1>
						<p>All links that can be found on Google Search are listed below.</p>
						<div class="code">
							<table>
								<xsl:for-each select="s:urlset/s:url">
									<tr>
										<td>
											<strong><xsl:value-of select="s:loc" /></strong>
											<br></br>
											Last modification: <xsl:value-of select="s:lastmod" />
											<br></br>
											Priority: <xsl:value-of select="s:priority" />
											<br></br>
											Images:
											<ol>
												<xsl:for-each select="image:image">
													<li>
														<xsl:value-of select="image:loc" />
													</li>
												</xsl:for-each>
											</ol>
										</td>
									</tr>
								</xsl:for-each>
							</table>
						</div>
					</div>
				</div>
				<div id="bottom"></div>
				<script src="frame.js"></script>
			</body>
		</html>
	</xsl:template>
</xsl:stylesheet>