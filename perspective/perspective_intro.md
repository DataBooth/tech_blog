[Perspective](https://perspective.finos.org) is a versatile data visualisation and analytics tool designed to handle large and streaming datasets efficiently. It allows users to create interactive reports, dashboards, and applications that can be customised according to their needs.

## Introductory examination - STATUS

I tried to run the tutorial examples (Jupyter notebooks) however got stuck on the basic imports. Logged an issue with developers. So putting on hold for now.


## Key Features

Perspective offers:

- Fast data processing capabilities
- Interactive visualisations
- Compatibility with both web browsers and Python environments
- Support for large datasets and real-time data streams

## Python Use Cases

The Python version of Perspective, called `perspective-python`, is particularly useful for:

**Data Analysis in Jupyter Notebooks**
Researchers and data scientists can use Perspective as a widget in Jupyter or JupyterLab to create interactive visualisations of their Pandas dataframes or Apache Arrow tables[1]. This allows for dynamic exploration of data within a familiar notebook environment.

**Building Data-Driven Applications**
Developers can use Perspective to create web applications that handle large datasets efficiently. The tool's ability to virtualise data means it only loads the necessary information for the current view, enabling smooth performance even with extremely large datasets[1].

**Real-Time Data Dashboards**
Perspective's support for streaming data makes it ideal for creating dashboards that update in real-time. This could be useful for monitoring financial markets, IoT sensor data, or any other scenario where live data visualisation is crucial[1].

**Scalable Data Exploration**
The Python API allows for the creation of interactive data exploration tools that can scale from small datasets to "ludicrous sise" datasets, making it suitable for a wide range of data analysis tasks[1].

By leveraging Perspective's capabilities through its Python API, users can create powerful, interactive data visualisation and analysis tools that work efficiently with large-scale and streaming data, bridging the gap between data processing and user-friendly presentation.

## DataGrid component - your Customisation Superpower

The DataGrid component in Perspective is a powerful and flexible tool that allows end users to customise their data views extensively. Here's an overview of its key features and customisation options:

## Interactive Column Management

Users can easily reorder, hide, or show columns by dragging and dropping or using context menus. This allows for quick customisation of the data view to focus on relevant information[1].

## Dynamic Sorting and Filtering

The DataGrid supports interactive sorting and filtering capabilities. Users can:

- Sort columns in ascending or descending order
- Apply filters to narrow down data based on specific criteria
- Use multiple filters simultaneously for complex data exploration

## Custom Styling

The DataGrid component supports extensive styling customisation:

- Users can apply custom CSS to change the appearance of cells, rows, and columns
- Conditional formatting can be implemented to highlight specific data points or trends[1]

## Aggregation and Pivoting

End users can perform on-the-fly data aggregations and pivoting:

- Group data by one or more columns
- Apply various aggregation functions (sum, average, count, etc.) to numerical columns
- Create pivot tables to analyze data from different perspectives

## Real-time Updates

The DataGrid efficiently handles real-time data updates, allowing users to see changes as they occur without performance degradation[1].

## Virtualisation for Large Datasets

Perspective's DataGrid uses virtualisation techniques to handle extremely large datasets smoothly, ensuring responsive performance even with millions of rows[1].

## Custom Cell Renderers

Advanced users can create custom cell renderers to display data in unique ways, such as:

- Inline charts or sparklines
- Custom formatting for specific data types
- Interactive elements within cells

## Keyboard Navigation and Accessibility

The DataGrid supports full keyboard navigation and is designed with accessibility in mind, ensuring that all users can effectively interact with and customise their data views.

## Export and Sharing

Users can easily export their customised views to various formats (CSV, JSON, etc.) or share specific configurations with other users.

By leveraging these features, end users can transform the default views they are provided into highly tailored, interactive data exploration tools that suit their specific needs and workflows. This level of customisation empowers users to gain deeper insights from their data without requiring extensive technical knowledge or developer intervention.

Citations:
[1] https://gist.github.com/texodus/c42f3189699bd29cf20bbe7dce767b07
[2] https://helpx.adobe.com/au/illustrator/using/perspective-drawing.html
[3] https://learn.microsoft.com/en-us/power-bi/create-reports/power-bi-personalise-visuals?tabs=powerbi-desktop
[4] https://data-marc.com/2020/08/18/power-bi-visual-customisation-using-perspectives/
[5] https://www.datahai.co.uk/power-bi/using-power-bis-personalised-visuals-as-a-stepping-stone-to-self-service-bi/
[6] https://www.youtube.com/watch?v=zwj7CtOGcuY
[7] https://www.youtube.com/watch?v=lIm9dHc8fOk
[8] https://perspective.finos.org/docs/js/


## Comparison with Power BI and Tableau-like tools

Perspective can be compared to other popular data visualisation tools like Power BI and Tableau in several key ways:

## Strengths of Perspective

**High-Performance Data Handling**
Perspective excels at processing and visualising large datasets efficiently. It can handle millions of rows of data smoothly, making it suitable for scenarios involving big data or real-time streaming[4].

**Flexibility and Customisation**
The tool offers a high degree of customisation, allowing developers to create tailored data exploration interfaces. This flexibility makes it well-suited for building specialised analytics applications[4].

**Cross-Platform Compatibility** 
Perspective works seamlessly in both web browsers and Python environments. This versatility allows it to be integrated into various workflows and platforms[4].

## Comparison with Power BI and Tableau

**Ease of Use**
Power BI and Tableau are generally considered more user-friendly for non-technical users. They offer drag-and-drop interfaces and a wide range of pre-built visualisations, making them accessible to business analysts without extensive coding knowledge.

**Data Modeling Capabilities**
Power BI has robust data modeling features, including the ability to create relationships between tables and define complex calculations. Tableau also offers data blending and preparation tools. Perspective, while powerful, may require more programming expertise for complex data transformations.

**Visualisation Options**
Tableau is renowned for its extensive visualisation capabilities and aesthetic appeal. Power BI also offers a wide range of chart types and customisation options. Perspective, while capable of creating various visualisations, may require more coding to achieve the same level of visual diversity.

**Enterprise Features**
Power BI and Tableau have more built-in features for enterprise-level reporting, such as scheduled refreshes, role-based access control, and integration with other business intelligence tools.

## Preferred Use Cases for Perspective

**Financial Analysis**
Perspective's ability to handle large datasets and real-time updates makes it particularly suitable for financial market analysis and trading applications.

**Scientific Research**
The tool's Python integration and performance with large datasets make it valuable for scientific data exploration and visualisation.

**Custom Analytics Applications**
Developers can leverage Perspective to build specialised data exploration tools tailored to specific industry needs or complex data structures.

**Real-Time Monitoring**
Perspective's support for streaming data makes it ideal for creating dashboards that require constant updates, such as IoT sensor monitoring or live system performance tracking.

While Power BI and Tableau excel in providing comprehensive business intelligence solutions for a wide range of users, Perspective shines in scenarios requiring high-performance data handling, extensive customisation, and integration with Python-based data science workflows.

Citations:
[1] https://community.fabric.microsoft.com/t5/Desktop/Perspectives-in-Power-BI/td-p/3579236
[2] https://www.datahai.co.uk/power-bi/using-power-bis-personalised-visuals-as-a-stepping-stone-to-self-service-bi/
[3] https://www.flip-design.de/?p=1014
[4] https://data-marc.com/2020/08/18/power-bi-visual-customisation-using-perspectives/
[5] https://www.youtube.com/watch?v=lIm9dHc8fOk
[6] https://community.fabric.microsoft.com/t5/Desktop/Can-I-use-perspectives-in-model-relationship-view/td-p/1741752
[7] https://www.youtube.com/watch?v=zwj7CtOGcuY
[8] https://community.fabric.microsoft.com/t5/Service/Perspectives-are-necessary-to-make-use-of-certain-types-of/m-p/3387672


I apologise for the confusion. Let me provide a comparison between Perspective and Apache Superset:

## Perspective vs Apache Superset

**Core Purpose**
Perspective is primarily a data visualisation and analytics library, while Apache Superset is a full-fledged business intelligence web application.

**Target Users**
- Perspective: Developers and data scientists who want to build custom data exploration tools
- Superset: Business analysts, data scientists, and non-technical users looking for a complete BI solution

## Key Differences

**Deployment**
- Perspective: Can be embedded in web applications or used within Python environments
- Superset: Typically deployed as a standalone web application

**Ease of Use**
- Perspective: Requires more programming knowledge, especially for complex visualisations
- Superset: Offers a user-friendly interface for creating visualisations and dashboards without coding

**Customisation**
- Perspective: Highly customisable through its API, allowing for tailored data exploration interfaces
- Superset: Customisable through its plugin architecture, but with a focus on out-of-the-box functionality

**Data Handling**
- Perspective: Excels at handling large datasets and real-time streaming data efficiently
- Superset: Can handle large datasets but may require more configuration for optimal performance with very large or streaming data

**Visualisation Types**
- Perspective: Focuses on interactive, high-performance visualisations, especially for financial and scientific data
- Superset: Offers a wide range of pre-built visualisations suitable for various business intelligence needs

## Strengths of Perspective

1. High-performance data handling, especially for large and streaming datasets
2. Flexibility for developers to create custom, interactive data exploration tools
3. Strong integration with Python data science workflows
4. Efficient for financial analysis and scientific research applications

## Strengths of Apache Superset

1. Comprehensive business intelligence solution with a user-friendly interface
2. Wide range of pre-built visualisations and dashboard creation tools
3. SQL Lab for advanced data exploration and query writing
4. Integration with various data sources and databases
5. Open-source with a strong community backing

## Use Case Comparison

**Financial Analysis**
- Perspective: Excels in creating custom, high-performance tools for real-time financial data analysis
- Superset: Offers pre-built visualisations and dashboards suitable for financial reporting and analysis

**Scientific Research**
- Perspective: Ideal for building specialised data exploration tools for complex scientific datasets
- Superset: Can be used for creating dashboards and reports from scientific data, but may require additional customisation

**Business Intelligence**
- Perspective: Can be used to build custom BI tools, but requires more development effort
- Superset: Provides a complete BI solution out-of-the-box, suitable for various business needs

In summary, Perspective is better suited for developers and data scientists who need to build custom, high-performance data exploration tools, especially for large or streaming datasets. Apache Superset, on the other hand, is a more comprehensive business intelligence solution that caters to a wider range of users and use cases, with less need for custom development.

Citations:
[1] https://www.restack.io/docs/superset-knowledge-apache-superset-vs-preset-comparison
[2] https://www.restack.io/docs/superset-knowledge-apache-superset-vs-competitors
[3] https://www.cloudthat.com/resources/blog/a-comparison-between-apache-superset-and-grafana
[4] https://superset.apache.org
[5] https://preset.io/blog/apache-superset-vs-tableau/
[6] https://trevor.io/blog/apache-superset-alternatives
[7] https://www.youtube.com/watch?v=lIm9dHc8fOk
[8] https://community.fabric.microsoft.com/t5/Service/Perspectives-are-necessary-to-make-use-of-certain-types-of/m-p/3387672