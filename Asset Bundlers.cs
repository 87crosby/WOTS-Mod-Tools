using System.Collections;
using System.Collections.Generic;
using UnityEditor;

public class CreateAssetBundles
{
	[MenuItem("Assets/Build AssetBundles")]
	static void BuildAllAssetBundles()
	{
		string assetBundleDirectory = "Assets/AssetBundles";
		if(!System.IO.Directory.Exists(assetBundleDirectory))
		{
			System.IO.Directory.CreateDirectory(assetBundleDirectory);
		}
		BuildPipeline.BuildAssetBundles (assetBundleDirectory, BuildAssetBundleOptions.UncompressedAssetBundle, BuildTarget.StandaloneWindows);
	}
}