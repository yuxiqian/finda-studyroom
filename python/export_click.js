// 页面内嵌的 js 脚本

// 当导出格式下拉框被更改时会执行这段代码

document.getElementById('ReportViewerControl_ctl01_ctl05_ctl01')
    .Controller.SetViewerLinkActive(
        document.getElementById('ReportViewerControl_ctl01_ctl05_ctl00')
            .selectedIndex != 0);

// 当点击导出按钮时会执行这段代码

var formatDropDown =
    document.getElementById('ReportViewerControl_ctl01_ctl05_ctl00');
if (formatDropDown.selectedIndex == 0) return false;
window.open(document.getElementById('ReportViewerControl')
                    .ClientController.m_exportUrlBase +
                encodeURIComponent(formatDropDown.value),
            '_blank')

// 这里的 m_exportUrlBase 猜测是
// "\/ReportServer\/Reserved.ReportViewerWebControl.axd?ExecutionID=ohrpuh553q1eoc45fl1bdrm3&ControlID=e7215cc0600146c8a62cb4aae1b46564&Culture=2052&UICulture=4&ReportStack=1&OpType=Export&FileName=LessonArrangeForOthers&ContentDisposition=OnlyHtmlInline&Format="

// encodeURIComponent encode 的就是 formatDropDown.value, 即
// "XML"、"CSV"、"TIFF"、"MHTML" 和 "EXCEL"。

// 跳转到的页面：

// http://electsysq.sjtu.edu.cn/ReportServer/Reserved.ReportViewerWebControl.axd?ExecutionID=2ibmxcr501ukz5zds2ky1v55&ControlID=a45be4edf6064ca6ae8056a78811be9a&Culture=2052&UICulture=4&ReportStack=1&OpType=Export&FileName=LessonArrangeForOthers&ContentDisposition=OnlyHtmlInline&Format=XML

formatDropDown.selectedIndex = 0;
document.getElementById('ReportViewerControl_ctl01_ctl05_ctl01')
    .Controller.SetViewerLinkActive(
        document.getElementById('ReportViewerControl_ctl01_ctl05_ctl00')
            .selectedIndex != 0);
return false;

// formatDropDown.value 可选值包括
// "XML"、"CSV"、"TIFF"、"MHTML" 和 "EXCEL"。
