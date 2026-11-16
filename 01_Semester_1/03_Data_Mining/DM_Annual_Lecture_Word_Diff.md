# فرق الكلمات الحرفي بين محاضرات 2025 ومواد 2026

هذا ملحق تفصيلي للملف `DM_Annual_Lecture_Literal_Audit.md`. يطبع الكلمات التي لا تقع في سلسلة مطابقة بين المصدرين. المقارنة تتجاهل الترقيم وحالة الأحرف لتسهيل محاذاة النص، وتحافظ على تهجئة الكلمات الظاهرة عند عرضها. كل `−` يعني نصًا في المصدر المؤرشف لا يقابله تسلسل مطابق في النص الحالي، وكل `+` يعني نصًا في مواد 2026 لا يقابله تسلسل مطابق في المؤرشف. الصياغة قد تكون معادَة المعنى بكلمات أخرى؛ لذلك «غير مطابق حرفيًا» لا يساوي تلقائيًا «محذوف مفهوميًا». الصور اليدوية متروكة للتفريغ البصري في التقرير الأساس لأن OCR لا يصلح لموازنة كلماتها.

## Data types, preparation, extraction, selection

**المصادر القديمة:** DM_Data_Preparation_Data_Types (archive).docx.  **مصادر 2026:** Week 02 - Basic Data Types in Data Mining (v2).docx, Week 03 - Feature Extraction and Portability.docx, Week4_Feature_Selection.docx.

**الكلمات المرمّزة:** القديم 7,900؛ الحالي 6,161؛ المتطابق بالترتيب 454. The 2025 file is one large combined document; the 2026 side concatenates Weeks 2–4 in course order.

1. − OLD [8–239]:
   and Machine Learning 1 Introduction In data science and machine learning understanding the type of data we
   are working with is crucial Different data types require different processing analysis and modeling
   techniques Broadly we classify data into two categories Nondependency Oriented Data Data where values are
   independent of each other Dependency Oriented Data Data where values are related or dependent on each other
   often involving order time or structure 2 Nondependency Oriented Data This type of data assumes that each
   record or object stands independently without sequential or structural dependencies 2 1 Quantitative
   Multidimensional Data Definition Data represented by multiple numerical attributes Example A medical dataset
   with patient information Age Blood Pressure Cholesterol Level BMI Characteristics Continuous values real
   numbers Can be represented in a vector form Use cases Regression clustering anomaly detection 2 2 Categorical
   and Mixed Attribute Data Categorical Data Attributes represent discrete categories labels Example Color Red
   Green Blue Country Kenya India USA Mixed Attribute Data Contains both numerical and categorical variables
   Example A student record Age 21 Gender Male GPA 3 4 Major Computer Science Challenges Need special encoding
   techniques e g one hot encoding Distance metrics are harder to define compared to numerical data 2 3 Binary
   and Set Data Binary Data Attributes with only two possible values 0 1 or True False Example Smoker Yes No
   Loan Defaulted Yes No Set Data Each object described by
   + 2026 [8–474]:
      1 Introduction Data Mining deals with different types of data Before applying a data mining technique it
      is important to understand What the data objects are What the attributes are What type of values the
      attributes contain How the data is organized or structured The type and structure of data influence which
      data mining technique should be used 2 Data Objects and Attributes Data Object A data object represents an
      entity about which information is collected Examples A patient A student A customer A transaction A
      document An image A geographic location For example Patient Age Gender BMI Diabetes P1 45 Male 28 5 Yes P2
      32 Female 24 1 No Here each row is a data object representing one patient Attribute An attribute is a
      property or characteristic of a data object For example Age Gender BMI Blood pressure Diabetes status 3
      Basic Types of Attributes This is an important part of Data Mining terminology 3 1 Nominal Attributes A
      nominal attribute contains categories with no natural order Examples Gender Male Female Color Red Blue
      Green Country Iraq Jordan Egypt Department CS IT Mathematics There is no meaningful ranking between the
      categories For example Male Female does not make sense 3 2 Ordinal Attributes An ordinal attribute
      contains categories with a meaningful order but the difference between categories is not necessarily
      measurable Examples Low Medium High Poor Good Excellent Small Medium Large Disease severity Mild Moderate
      Severe For example Low Medium High The order is meaningful but we cannot say that the difference between
      Low and Medium is exactly the same as the difference between Medium and High 3 3 Binary Attributes A
      binary attribute has only two possible values Examples Yes No True False 0 1 Disease No Disease Purchased
      Not Purchased For example Patient Diabetes P1 1 P2 0 Binary attributes are very common in classification
      and association analysis 3 4 Numerical Attributes Numerical attributes contain quantitative numerical
      values Examples Age Height Weight Temperature Salary Blood pressure Numerical attributes can be divided
      into Discrete Numerical Attributes Values are generally countable Examples Number of children Number of
      transactions Number of students Number of visits For example Number of children 0 1 2 3 Continuous
      Numerical Attributes Values can take many values within a range Examples Height 175 5 cm Weight 72 4 kg
      Temperature 36 7 C Blood glucose 125 6 mg dL 4 Basic Data Structures in Data Mining After explaining
      attribute types we can explain how complete datasets are organized 4 1 Record Data Record data consists of
      a collection of records where each record contains a set of attributes Example Student Age GPA Department
      S1 20 3 1 CS S2 22 3 6 IT S3 21 2 9 CS Applications Classification Clustering Regression Outlier detection
      4 2 Transaction Data Each transaction contains
2. − OLD [245–532]:
   A market basket with purchased items Milk Bread Eggs Applications Association rule mining e g Market Basket
   Analysis Recommendation systems 2 4 Text Data Definition Data stored as unstructured textual information
   Examples Emails articles reviews tweets Challenges Text is unstructured and must be converted into numerical
   form Bag of Words TF IDF word embeddings Applications Sentiment analysis topic modeling chatbots search
   engines 3 Dependency Oriented Data This type of data considers relationships order and structure among data
   elements 3 1 Time Series Data Definition A sequence of values recorded over time Example Stock prices weather
   data ECG signals Characteristics Temporal dependency past values influence future values Often analyzed using
   ARIMA LSTMs Transformers Applications Forecasting anomaly detection 3 2 Discrete Sequences and Strings
   Definition Data represented as sequences of discrete symbols Examples DNA RNA sequences ATCG Clickstreams
   sequence of web pages visited Challenges Pattern matching alignment and subsequence analysis Applications
   Bioinformatics web usage mining natural language processing 3 3 Spatial Data Definition Data representing
   objects in a spatial or geographical context Examples Maps satellite images urban planning data Coordinates
   of locations latitude longitude Challenges Spatial autocorrelation nearby objects are more related
   Applications GIS Geographic Information Systems traffic monitoring environmental modeling 3 4 Network and
   Graph Data Definition Data represented as nodes and edges Examples Social networks Facebook users nodes
   friendships edges Citation networks papers citing each other Characteristics Strongly structured data
   Requires graph algorithms PageRank community detection Graph Neural Networks Applications Social media
   analysis fraud detection recommender systems 4 Summary Nondependency Oriented Data includes numerical vectors
   categorical mixed data binary set data and text Dependency Oriented Data includes time series sequences
   spatial and graph data Each data type requires different preprocessing methods similarity measures and
   analytical models Data Preparation
   + 2026 [480–930]:
      Transaction 1 Bread Milk Eggs Transaction 2 Bread Butter Transaction 3 Milk Eggs Juice This type of data
      is commonly used in Association Rule Mining Example Bread Milk This may indicate that customers who buy
      bread often buy milk 4 3 Text and Document Data Text data includes Documents Emails News articles Research
      papers Customer reviews Social media posts Example This product is excellent and easy to use Data Mining
      techniques can identify Frequent words Topics Sentiment Document similarity Text classification This area
      is commonly called Text Mining 4 4 Sequence Data Sequence data contains elements in a specific order
      Example A B C D Examples include DNA sequences Customer purchasing sequences Web click sequences User
      activity sequences The order is important For example Login Search Product Purchase may represent a
      customer's browsing behavior 4 5 Time Series Temporal Data Temporal data contains observations associated
      with time Example Month Temperature January 12 C February 15 C March 19 C Examples Stock prices Weather
      data Rainfall Electricity consumption Patient monitoring Sensor measurements Data Mining can discover
      Trends Seasonal patterns Periodic patterns Anomalies 4 6 Spatial Data Spatial data represents objects or
      observations associated with geographic or physical locations Examples Maps Satellite images GPS
      coordinates Roads Population distributions Environmental measurements For example Location A 32 48 45 82
      Spatial Data Mining can discover relationships between objects based on their locations 4 7 Image and
      Multimedia Data Image data contains information represented as pixels A grayscale image can be represented
      as a 2D matrix Height Width A color RGB image can be represented as Height Width 3 Examples X ray images
      MRI images CT images Satellite images Facial images Histopathology images Image Mining can identify
      Objects Shapes Patterns Textures Regions Common methods include CNNs and other deep learning models 4 8
      Graph and Network Data Graph data represents relationships between objects A graph consists mainly of
      Nodes vertices objects Edges relationships Example Student A Student B could represent a friendship
      Examples Social networks Computer networks Citation networks Transportation networks Financial networks
      Knowledge graphs Graph Mining can discover Communities Important nodes Relationships Frequent structures
      Paths 5 Summary It is useful to distinguish between attribute types and data structures Category Examples
      Nominal Gender country color Ordinal Low Medium High Binary Yes No 0 1 Numerical Age weight temperature
      Record Data Student patient tables Transaction Data Shopping baskets Text Data Documents reviews Sequence
      Data DNA click sequences Temporal Data Stock prices rainfall Spatial Data Maps GPS Image Data X rays MRI
      Graph Data Social networks Nominal ordinal binary and numerical describe attributes Record transaction
      text sequence temporal spatial image and graph data describe how the data is organized or represented Data
      Preparation in Data Mining 1 Introduction
3. − OLD [539–963]:
   collecting cleaning transforming and organizing raw data into a usable format before it is fed into a
   database analytical system or machine learning model The data preparation phase is a multistage process that
   comprises several individual steps some or all of which may be used in a given application These steps are as
   follows Feature extraction and portability The raw data is often in a form that is not suitable for
   processing Examples include raw logs documents semistructured data and possibly other forms of heterogeneous
   data Data Collection Gathering data from multiple sources databases files APIs sensors etc Data Cleaning
   Handling missing values removing duplicates correcting errors and resolving inconsistencies Data Integration
   Combining data from different sources into a single coherent dataset Data Transformation Converting data into
   a consistent format e g encoding categorical variables normalization scaling Data Reduction Reducing the size
   dimensionality of data by removing irrelevant features or aggregating values Data Splitting Dividing data
   into training validation and test sets in machine learning tasks Why is Data Preparation Important Ensures
   accuracy removes errors and inconsistencies Improves efficiency organized data is faster to process Enhances
   model performance clean balanced and relevant data leads to better predictions Supports better decision
   making reliable insights come from well prepared data In short Data preparation turns raw messy data into
   high quality structured data that is ready for analysis or modeling What is Feature Extraction Feature
   extraction is the process of deriving new more informative features from raw data to improve analysis or
   model performance Instead of using raw data directly we transform it into meaningful variables features
   Especially important in machine learning image processing text mining and signal processing Why Feature
   Extraction is Important Raw data may be too complex or noisy for direct use Helps reduce dimensionality fewer
   but more meaningful features Makes patterns in data more detectable for algorithms Improves accuracy and
   efficiency of models Examples of Feature Extraction From Images Extracting edges textures color histograms or
   deep learning embeddings e g from CNN layers Example From a breast cancer X ray extracting shape and texture
   features From Text Converting words into numerical features using TF IDF bag of words or word embeddings
   Word2Vec BERT Example Extracting keywords from medical notes From Audio Signals Extracting frequency
   amplitude or MFCC features from sound signals Example Identifying heart murmurs in ECG recordings From
   Tabular Data Creating derived attributes such as BMI from weight height or Age Group from raw age Where Does
   It Fit in the Multistage Process Data Preparation Pipeline with Feature Extraction included Data Collection
   + 2026 [937–1025]:
      preparing raw data so that it can be used effectively by Data Mining algorithms Real world data is often
      Incomplete Noisy Inconsistent Duplicated In different formats Containing irrelevant attributes Containing
      different scales of numerical values Therefore data usually needs to be prepared before applying data
      mining techniques Basic process Raw Data Data Preparation Data Mining Knowledge Patterns The quality of
      the prepared data can strongly affect the quality of the discovered patterns and the performance of the
      mining model 2 Main Steps of Data Preparation Data preparation commonly includes
4. − OLD [970–1436]:
   scaling encoding Feature Extraction deriving new useful features Data Reduction optional to eliminate
   irrelevant features Data Splitting for ML tasks Data Type Portability Numeric to Categorical Data
   Discretization What is Discretization Discretization is the process of converting continuous numeric data
   into discrete categorical data by dividing the range of values into intervals bins Each interval is then
   assigned a category label It helps simplify data and makes it easier for algorithms especially classification
   models or rule based systems to work with Why Use Discretization Some algorithms like decision trees Na ve
   Bayes work better with categorical data Reduces the effect of noise in continuous values Makes data more
   interpretable for humans e g age groups instead of raw age Helps in detecting non linear relationships Types
   of Discretization Equal Width Binning Divides the range of values into equal sized intervals Example Age 0
   100 divided into bins 0 20 21 40 41 60 61 80 81 100 Equal Frequency Binning Quantile Binning Each bin has
   approximately the same number of data points Example Splitting 100 students scores into 4 bins with 25
   students each Clustering Based Discretization Uses clustering e g k means to group values into categories
   Supervised Discretization Considers class labels when forming bins Example Split income into bins that best
   separate loan approved vs loan rejected Example Suppose we have a numeric attribute Age 15 18 22 35 42 50 63
   70 Equal Width Binning width 20 Categories Teen 0 20 Young 21 40 Middle aged 41 60 Senior 61 80 Result Teen
   Teen Young Young Middle aged Middle aged Senior Senior Equal Frequency Binning 2 bins Categories Low age
   first 4 values High age last 4 values Result Low Low Low Low High High High High Categorical to Numeric Data
   Binarization What is Binarization Binarization is the process of converting categorical data or sometimes
   continuous data into numeric binary form 0s and 1s Each category or condition is represented as a binary
   feature A special case of encoding categorical variables Why Use Binarization Machine learning algorithms
   like regression SVMs neural networks require numeric inputs not raw text labels Makes categorical attributes
   usable in computations Helps represent presence absence of a feature Types of Binarization One Hot Encoding
   Each category gets a new binary column Example Color Red Blue Green Red Blue Green 1 0 0 Red 0 1 0 Blue 0 0 1
   Green Label Binarization Binary Thresholding Converts a single attribute into binary values based on a
   threshold Example Income 50K 1 else 0 Multi Label Binarization Used when items can belong to multiple
   categories simultaneously Example Movie genres Action Comedy Drama Action Comedy Drama 1 1 0 Action Comedy
   movie 0 1 1 Comedy Drama movie Example Suppose we have Fruit Apple Banana Orange Apple One Hot Binarization
   Apple Banana Orange
   + 2026 [1032–1935]:
      Data Reduction Data Discretization These steps are not necessarily performed in exactly the same order for
      every dataset 3 Data Cleaning Data Cleaning is the process of detecting and correcting problems in the
      data Common problems include Missing values Noisy data Outliers Duplicate records Inconsistent data 3 1
      Missing Values A missing value occurs when information for an attribute is not available Example Patient
      Age Weight Blood Pressure P1 45 72 120 P2 38 130 P3 51 80 Here Weight for P2 and Blood Pressure for P3 are
      missing Why are missing values a problem Many Data Mining algorithms cannot directly work with missing
      values or their performance may be affected Methods for Handling Missing Values Method 1 Ignore the record
      The record containing missing data may be removed This can be reasonable when only a very small number of
      records have missing values However removing many records can result in loss of useful information Method
      2 Fill in the value manually A domain expert may determine the missing value For example a doctor may
      determine an appropriate value based on other medical information Method 3 Use the mean For numerical data
      the missing value can be replaced by the mean Example Values 60 70 80 90 Mean 60 70 80 90 4 75 Therefore
      75 Method 4 Use the median The median can be used instead of the mean especially when the data contains
      extreme values Example 60 65 70 75 200 The value 200 is an extreme value so the median may be more
      appropriate than the mean Method 5 Use the mode For categorical data the missing value can be replaced by
      the mode which is the most frequently occurring value Example Gender Male Female Male Male The missing
      value could be replaced with Male Method 6 Predict the missing value A Data Mining or Machine Learning
      method can be used to estimate the missing value Examples Regression Decision tree k NN Other predictive
      models 4 Noisy Data Noise refers to random errors or unwanted variation in the data Example Suppose the
      actual ages are 21 22 23 24 25 but the dataset contains 21 22 223 24 25 The value 223 may be a data entry
      error Methods for Handling Noise Common approaches include Binning Regression Clustering Outlier detection
      4 1 Binning Binning divides numerical values into groups called bins Example 10 12 13 20 22 25 30 31 We
      could create Bin 1 10 13 Bin 2 20 25 Bin 3 30 31 Binning can help smooth noisy numerical data 5 Outliers
      An outlier is a data object whose value is significantly different from most other observations Example 65
      67 68 70 69 300 The value 300 is potentially an outlier However an important point is An outlier is not
      necessarily an error For example a patient's blood pressure may be unusually high because the patient
      actually has a medical condition Therefore outliers should be investigated before removing them Methods
      for detecting outliers Statistical methods Distance based methods Clustering Visualization Machine
      Learning methods 6 Duplicate Data Duplicate data occurs when the same data object appears more than once
      Example ID Name Age 101 Ahmed 45 102 Ali 38 101 Ahmed 45 The first and third records may represent the
      same object Duplicate records can Increase dataset size unnecessarily Bias the analysis Affect frequency
      calculations Affect model performance Therefore duplicate records should be identified and handled
      appropriately 7 Inconsistent Data Data can also contain inconsistencies Example Student Gender S1 Male S2
      M S3 male S4 Female These values may represent the same categories but use different formats They can be
      standardized as Male Female Similarly Iraq IRAQ iraq can be standardized as Iraq 8 Data Integration Data
      Integration combines data from multiple sources into a single dataset For example a university may have
      Database 1 Student information ID Name Department Database 2 Student grades Student ID GPA These datasets
      can be integrated using the student ID Problems in Data Integration Different attribute names Different
      data formats Duplicate records Different units Different database schemas Example One database uses Weight
      kg Another uses Weight pounds These values must be converted to a consistent unit 9 Data Transformation
      Data Transformation converts data into a suitable format for Data Mining algorithms Common transformation
      techniques include Normalization Aggregation Generalization Encoding Feature construction 10 Normalization
      Normalization is used to transform numerical values into a similar scale This is important when attributes
      have very different ranges Example Attribute Range Age 0 100 Salary 300 10 000 Income 1 000 100 000 A
      large numerical range can dominate some algorithms 10 1 Min Max Normalization A common formula is This
      usually transforms values into the range 0 to 1 Example Suppose Minimum age 20 Maximum age 60 Age 40 Then
      So 40 years 0 5 10 2 Z Score Normalization Another common method is Z score normalization where original
      value mean standard deviation After transformation the data is represented relative to its mean and
      standard deviation 11 Encoding Categorical Data Many Data Mining and Machine Learning algorithms require
      numerical input Therefore categorical values may need to be converted into numerical representations
      Example Gender Male Female Female Male One simple encoding could be Male 1 Female 0 However this approach
      should be used carefully because numerical codes can incorrectly imply an order For categories such as Red
      Blue Green One hot encoding is often more appropriate Red Blue Green
5. − OLD [1446–3513]:
   1 0 0 Threshold Binarization e g Fruit Apple 1 0 Fruit is Apple 1 0 0 Text to Numeric Data 1 Introduction
   Many datasets contain textual data reviews documents social media posts medical notes etc Machine learning
   algorithms cannot directly process text because they work with numbers matrices vectors Hence we need to
   convert text into numeric form this process is called Text Representation or Feature Extraction from Text 2
   Why Convert Text to Numeric Algorithms like logistic regression decision trees SVMs and neural networks
   require numeric input Text to numeric conversion enables Sentiment Analysis positive negative reviews Spam
   Filtering email classification Document Clustering grouping news articles Language Modeling speech
   recognition chatbots 3 Methods of Converting Text to Numeric 3 1 Traditional Statistical Methods Bag of Words
   BoW Represents text as a vector of word counts Example Sentence 1 The cat sat on the mat Sentence 2 The dog
   sat on the log Vocabulary cat dog mat log sat the on Sentence 1 1 0 1 0 1 2 1 Pros Simple fast Cons Ignores
   word order and context TF IDF Term Frequency Inverse Document Frequency Adjusts BoW by giving higher weight
   to important words and lower weight to common ones Formula TF IDF t d TF t d IDF t TF text IDF t d TF t d
   times IDF t TF IDF t d TF t d IDF t Example Words like the or is get low weight while cancer or finance get
   higher weight Better than BoW because it reduces the impact of frequent but uninformative words 3 2
   Distributed Representations Dense Vectors Word Embeddings Represent words in dense vectors instead of sparse
   matrices Words with similar meaning have similar vectors Examples Word2Vec GloVe FastText Advantage Captures
   semantic relationships king man woman queen Sentence Embeddings Represent entire sentences as vectors Example
   Doc2Vec Sentence BERT SBERT Useful for classification clustering and semantic similarity 3 3 Deep Learning
   Based Representations Recurrent Neural Networks RNNs Capture word sequences context aware Often used for
   language modeling speech recognition Transformers BERT GPT etc State of the art models for text understanding
   Convert text into contextual embeddings meaning the same word has different vectors depending on context
   Example bank in river bank vs money bank different embeddings 4 Examples Email Spam Detection Convert emails
   into TF IDF vectors feed into Na ve Bayes Movie Reviews Sentiment Analysis Use Word2Vec or BERT embeddings
   classify as positive negative Search Engines Use sentence embeddings to find documents similar to a query 5
   Challenges in Text to Numeric Conversion High dimensionality huge vocabulary Data sparsity most entries in
   BoW TF IDF are zeros Context loss BoW ignores word order Ambiguity words have multiple meanings 6 Best
   Practices For small datasets Use BoW or TF IDF For medium datasets Use pre trained embeddings Word2Vec GloVe
   For large datasets high performance tasks Use transformer models BERT GPT RoBERTa Summary Text to numeric
   conversion transforms unstructured textual data into structured numeric vectors Common approaches include BoW
   and TF IDF traditional word sentence embeddings distributed and transformers deep learning The right method
   depends on dataset size computational resources and task complexity Time Series to Discrete Sequence Data 1
   Introduction Time series data A sequence of values recorded over time e g stock prices ECG signals
   temperature readings Sometimes instead of working with raw continuous numeric time series values it is
   beneficial to convert them into discrete sequences of symbols or states This transformation is useful for
   pattern recognition compression anomaly detection and symbolic data mining Example Instead of keeping raw
   heart rate values 75 77 80 60 58 90 we can convert them into symbols like N N H L L H where N Normal H High L
   Low 2 Why Convert Time Series to Discrete Sequences Simplicity Discrete sequences are easier to store analyze
   and interpret Pattern discovery Helps detect recurring patterns motifs or unusual sequences anomalies Noise
   reduction Removes minor fluctuations in continuous signals Compatibility Many algorithms string matching
   Markov models HMMs work better with symbolic sequences 3 Techniques for Conversion 3 1 Symbolic
   Representation Assign symbols discrete states to numeric ranges Example If temperature 20 C C Cold If 20 30 C
   M Mild If 30 C H Hot Original series 18 22 28 35 31 19 Converted sequence C M M H H C 3 2 Discretization by
   Quantization Divide the numeric values into fixed bins intervals Example Stock price movements 1 decrease 0
   stable 1 increase Prices 100 102 101 103 107 Sequence 1 1 1 1 3 3 Symbolic Aggregate Approximation SAX A
   popular method in time series data mining Steps Normalize the series mean 0 variance 1 Divide series into
   equal sized segments Compute average value for each segment Map averages into symbols using breakpoints
   Advantage Reduces dimensionality while keeping essential patterns 3 4 Piecewise Aggregate Approximation PAA
   Symbolization Split time series into equal intervals Replace each interval with its mean Convert those means
   into discrete symbols 3 5 Hidden Markov Models HMM Model time series as sequences of hidden states Example
   Speech recognition sound wave phoneme sequence 3 6 Trend Based Encoding Encode only directional changes up
   down stable Example Stock series 100 105 103 103 110 Sequence U D S U U Up D Down S Stable 4 Applications
   Healthcare ECG signals symbolic sequences for anomaly detection Finance Stock price changes sequences of up
   down for pattern discovery IoT Sensors Temperature humidity readings symbolic states Speech recognition Sound
   waves phoneme sequences Bioinformatics DNA microarray time series gene expression states 5 Advantages
   Limitations Method Advantages Limitations Symbolic thresholds Simple intuitive Sensitive to threshold choice
   Quantization Reduces complexity May lose detail SAX Dimensionality reduction noise tolerant Requires careful
   parameter tuning PAA Symbols Captures trends Loses fine grained info HMM Captures temporal dependencies
   Computationally expensive Trend Encoding Good for direction patterns Ignores magnitude 6 Summary Converting
   time series to discrete sequences helps simplify analysis reduce noise and apply symbolic machine learning
   techniques Common approaches include thresholding quantization SAX PAA HMM and trend encoding The choice of
   method depends on the application simple thresholds for quick categorization SAX for large scale mining and
   HMM for sequential modeling Time Series to Numeric Data 1 Introduction A time series is a sequence of
   observations collected at regular intervals e g stock prices daily temperatures ECG signals Many machine
   learning algorithms regression classification clustering work best with fixed length numeric feature vectors
   Therefore converting time series numeric data is essential for enabling ML models to process and analyze
   temporal patterns 2 Why Convert Time Series to Numeric Compatibility Most ML algorithms require fixed size
   vectors not sequences Efficiency Numeric summaries reduce high dimensional time series data into compact
   representations Feature Engineering Numeric features capture important characteristics of the signal Pattern
   Detection Enables classification regression or clustering on time series datasets 3 Methods for Conversion 3
   1 Statistical Feature Extraction Extract descriptive statistics from the time series Mean average value of
   the series Standard deviation variance variability Min max extremes Skewness kurtosis distribution shape
   Percentiles e g median 25th 75th quantiles Example For daily temperature 20 22 25 23 19 features could be
   Mean 21 8 Std 2 3 Min 19 Max 25 3 2 Temporal Features Capture time related characteristics Trend increasing
   decreasing slope Seasonality daily weekly monthly cycles Autocorrelation coefficients relationship with past
   values Lag features shifted versions of the series Example Electricity consumption extract daily peak off
   peak and average usage 3 3 Frequency Domain Features Transform time series into the frequency domain using
   Fourier or Wavelet transforms Fourier Transform FFT Extract dominant frequency energy spectrum Wavelet
   Transform Captures both time and frequency characteristics Example ECG extract heart rate frequency
   components 3 4 Shape Based Features Dynamic Time Warping DTW distance to reference series Shapelets Small
   subsequences highly discriminative for classification 3 5 Window Based Feature Extraction Divide series into
   windows segments Extract features from each window mean slope variance Useful for long time series data 3 6
   Dimensionality Reduction Approaches Convert time series into numeric embeddings using Principal Component
   Analysis PCA Reduces time series dimensions Autoencoders Neural networks that learn compressed numeric
   representations SAX Symbolic Aggregate Approximation Vectorization Convert symbolic sequences into numeric
   histograms 3 7 Pretrained Time Series Embeddings Use models like TS2Vec or Time2Vec that map variable length
   time series into fixed length numeric vectors Useful in deep learning tasks 4 Applications Finance Stock
   price series volatility moving averages numeric features for prediction Healthcare ECG EEG frequency domain
   features for disease detection IoT Sensors Temperature pressure readings numeric summaries for fault
   detection Speech Recognition Audio waveforms MFCCs Mel frequency cepstral coefficients 5 Advantages
   Limitations Method Advantages Limitations Statistical Features Simple interpretable May miss temporal
   dynamics Temporal Features Captures trends cycles Requires careful lag selection Frequency Features Reveals
   hidden periodicity Can be complex computationally heavy Shapelets DTW Captures local patterns Sensitive to
   noise Dimensionality Reduction Handles high dimensionality Risk of info loss 6 Summary Time series numeric
   data is essential for applying machine learning models Approaches include statistical features temporal
   dynamics frequency transforms shapelets and embeddings The choice depends on the application Quick summaries
   statistical features Cyclical patterns temporal frequency features Deep learning tasks embeddings or
   autoencoders Discrete Sequence to Numeric Data 1 Introduction Discrete sequences are sequences of symbols or
   categorical values ordered in time or position Examples DNA sequence A T G C A Protein sequence M K L V
   Clickstream Home Search Product Checkout Problem Machine learning algorithms require numeric input Solution
   Convert discrete sequences into numeric feature vectors while preserving sequence information 2 Why Convert
   Sequences to Numeric Compatibility Most ML models SVM Random Forest Neural Networks cannot process symbols
   directly Pattern Detection Enables classification clustering and regression on sequence data Dimensionality
   Reduction Represent sequences as fixed length numeric vectors Similarity Computation Numeric vectors allow
   distance metrics for clustering or nearest neighbor search 3 Methods of Conversion 3 1 One Hot Encoding Each
   symbol becomes a binary vector Example DNA A T G C 4 dimensional vector A 1 0 0 0 T 0 1 0 0 For sequences
   concatenate vectors very high dimensional vectors for long sequences 3 2 k mer or n gram Counts Break
   sequences into subsequences of length k and count occurrences Example DNA sequence ATGCAT with k 2 dimers
   Substrings AT TG GC CA AT Count vector AT 2 TG 1 GC 1 CA 1 Produces fixed length numeric representation for
   sequences of varying lengths 3 3 Frequency Based Vectors Count the frequency of symbols in the sequence
   Example DNA sequence ATGCAT A 2 T 2 G 1 C 1 Numeric vector 2 2 1 1 Simple but ignores order or local patterns
   3 4 Position Specific Encoding Preserve order information encode symbol position Example Sequence length 5
   DNA alphabet size 4 5 4 20 dimensional binary vector Useful for sequence classification tasks 3 5 Embeddings
   for Sequences Similar to word embeddings in NLP map symbols to dense numeric vectors Example DNA2Vec ProtVec
   Node2Vec for graphs Advantage Captures similarity and context among symbols 3 6 Sequence Alignment Distance
   Based Features Compute similarity or distance between sequences and a reference set Hamming distance
   Levenshtein distance Convert distances to numeric features for ML Example Sequence classification using
   nearest neighbors 3 7 Bag of Patterns or Symbolic Aggregate Approximation SAX Convert sequences into symbolic
   patterns motifs first Count pattern occurrences numeric feature vector Useful for time series sequences
   converted into discrete symbols 4 Applications Bioinformatics DNA protein classification gene prediction Web
   Analytics Clickstream analysis for user behavior modeling Speech Processing Phoneme sequences numeric
   features Text Analysis Convert sequences of words into numeric vectors for classification 5 Advantages
   Limitations Method Advantages Limitations One Hot Encoding Simple interpretable Very high dimensional for
   long sequences k mer n gram counts Captures local patterns May ignore global sequence info Frequency vectors
   Low dimensional Ignores order Embeddings Captures similarity context Requires pretraining or large data
   Distance based features Preserves sequence similarity Computation heavy for large datasets 6 Summary Discrete
   sequences must be converted into numeric features for machine learning Common methods include One hot
   encoding k mer n gram counts Frequency based vectors Embeddings Distance based features Choice depends on
   sequence length pattern importance and computational resources Spatial to Numeric Data 1 Introduction Spatial
   data represents objects or events that have a location in space Examples include Geographic coordinates
   Latitude Longitude e g cities landmarks Maps of regions buildings roads Medical imaging tumor shapes organ
   boundaries Satellite images GIS datasets Problem
   + 2026 [1945–3171]:
      12 Data Reduction Sometimes a dataset is very large and contains many attributes or records Data Reduction
      attempts to reduce the size or complexity of the data while preserving important information Common
      techniques include Dimensionality reduction Feature selection Sampling Aggregation Numerosity reduction 12
      1 Feature Selection Feature Selection selects the most useful attributes and removes irrelevant or
      redundant ones Example Suppose a dataset contains Age Gender BMI Blood Pressure Patient Name Phone Number
      Address If the goal is disease prediction some attributes may be irrelevant Feature selection might retain
      Age Gender BMI Blood Pressure and remove attributes that do not contribute useful information Important
      distinction Feature Selection Select existing features Feature Extraction Create new features from the
      original features For example Selecting Age Feature Selection PCA creating new components Feature
      Extraction 13 Dimensionality Reduction Dimensionality reduction reduces the number of attributes while
      attempting to preserve important information A common technique is Principal Component Analysis PCA For
      example 100 original features 10 principal components This can reduce Computational cost Storage
      requirements Model complexity and may help with visualization 14 Data Discretization Discretization
      converts continuous numerical values into intervals or categories Example Age 18 25 32 47 65 72 can be
      transformed into Age Category 18 Young 25 Young 32 Adult 47 Adult 65 Senior 72 Senior For example 0 17
      Child 18 35 Young Adult 36 60 Adult 61 Senior Discretization can make some datasets easier to analyze 15
      Data Preparation and Data Mining The overall process can be represented as Raw Data Data Cleaning Data
      Integration Data Transformation Data Reduction Data Discretization Prepared Data Data Mining Algorithm
      Patterns Knowledge However these steps are not always mandatory or performed in exactly this order The
      appropriate preparation depends on the dataset and the mining task 16 Example Medical Dataset Suppose we
      have a diabetes dataset Age Glucose BMI Gender Diabetes 45 140 31 5 Female Yes 32 24 2 Male No 51 180 35 1
      Female Yes 29 110 22 8 Male No Before applying a classification algorithm we may Step 1 Handle missing
      values Glucose for the second patient is missing Replace it using an appropriate method Step 2 Check for
      outliers Check whether values such as glucose or BMI contain unusual observations Step 3 Encode
      categorical data Convert Gender into a suitable numerical representation Step 4 Normalize numerical
      attributes If required by the selected algorithm normalize Age Glucose BMI Step 5 Select useful features
      Remove irrelevant attributes if necessary Step 6 Apply Data Mining Use a classification algorithm such as
      Decision Tree Na ve Bayes k NN Logistic Regression Random Forest 17 Data Preparation vs Data Preprocessing
      These terms are sometimes used interchangeably but there is a useful distinction Data Preparation A
      broader process that prepares data for analysis or Data Mining It may include Cleaning Integration
      Transformation Reduction Discretization Data Preprocessing Often refers more specifically to operations
      performed before modeling such as Handling missing values Removing noise Encoding Scaling normalization
      Feature selection Therefore Data preprocessing can be considered an important part of the broader data
      preparation process The exact terminology can vary between textbooks and research papers 18 Important
      Points to Remember Data Cleaning Deals with problems in the data Missing values noise outliers duplicates
      inconsistencies Data Integration Combines data from different sources Databases files systems Data
      Transformation Changes data into a suitable representation Normalization encoding aggregation Data
      Reduction Reduces data size or dimensionality Feature selection PCA sampling Data Discretization Converts
      continuous values into intervals Age Young Adult Senior 19 Summary Data Preparation is an essential stage
      of Data Mining The main activities are Data Cleaning correct or handle incomplete noisy inconsistent and
      duplicate data Data Integration combine data from multiple sources Data Transformation convert data into a
      suitable format Data Reduction reduce the size or dimensionality of data Data Discretization convert
      continuous values into discrete intervals Main idea Good data preparation Better quality data More
      reliable data mining results And an important teaching point for your Data Mining course is Data
      Preparation is not simply removing missing values It is the complete process of making raw data suitable
      for discovering useful patterns and knowledge Feature Extraction and Portability Feature extraction
      Feature extraction is the process of creating new features from existing data to represent its important
      characteristics in a form suitable for data mining or machine learning algorithms Obtains useful
      characteristics from the data Example Suppose we have a medical X ray image X ray Image Feature Extraction
      Texture shape edges intensity Numerical Features Classification Instead of giving the complete image
      directly to a traditional algorithm we can represent it using useful features Why Do We Need Feature
      Extraction Raw data can be very large complex difficult to process high dimensional unsuitable for some
      algorithms Feature extraction can Reduce the amount of data Remove unnecessary information Represent
      important characteristics of the data Make data easier for algorithms to process Sometimes improve
      prediction or classification performance Examples of Feature Extraction Different types of data require
      different extraction methods Data Type Possible Extracted Features Image Shape texture edges color Text
      Word frequency TF IDF embeddings Time Series Mean variance frequency components Audio Frequency energy
      spectral features Spatial Distance density location features Sequence Symbol frequencies patterns Graph
      Degree centrality connectivity Data Type Portability In Data Mining data can appear in many different
      forms Examples Numerical data Age 25 Salary 800 000 Categorical data Gender Male Female Text data Medical
      reports emails reviews Time series data Heart rate recorded every second Image data X rays CT scans
      Spatial data Locations and maps Sequence data DNA sequences Graph data Social networks Data Type
      Portability means converting data from one representation or type into another representation so that it
      can be processed by a data mining algorithm Why Do We Need Data Type Portability A dataset may contain
      several types of information at the same time For example a medical dataset may contain age gender medical
      reports and heart rate measurements Different algorithms are designed to work with different forms of data
      Therefore some data may need to be converted into a suitable representation before applying a data mining
      algorithm Basic process Different Data Types Data Type Conversion Suitable Representation Data Mining
      Algorithm Common Data Type Conversions Numerical Categorical Discretization Categorical Numerical Encoding
      Text Numerical Vectorization Time Series Sequence Symbolic representation Time Series Numerical features
      DFT DWT or feature extraction Image Numerical features Feature extraction Graph Numerical representation
      Graph embedding Any data type Graph Similarity graph Numerical Data Categorical Data A common conversion
      is discretization Discretization converts continuous numerical values into a small number of categories or
      intervals Example 0 17 Young 18 40 Adult 41 60 Middle aged 61 Older Thus 25 Adult 45 Middle aged 67 Older
      Advantages Makes numerical data easier to understand Can make data suitable for algorithms that require
      categorical values Disadvantage Some information can be lost For example ages 21 and 39 may both become
      Adult so their exact difference is no longer represented Types of Discretization Equal Width
      Discretization The numerical range is divided into intervals of approximately equal numerical size Example
      Age 0 80 divided into 0 20 21 40 41 60 61 80 Equal Frequency Discretization Each interval contains
      approximately the same number of observations Example 10 12 15 18 20 30 35 40 Two groups Group 1 10 12 15
      18 Group 2 20 30 35 40 Categorical Data Numerical Data
6. − OLD [3519–6207]:
   numeric feature vectors so spatial data must be converted into numeric representations 2 Why Convert Spatial
   Data to Numeric Compatibility ML algorithms cannot process raw spatial objects like polygons or graphs
   Feature Engineering Extract numeric attributes that capture spatial relationships and shapes Distance
   Computation Numeric coordinates allow calculation of distances similarity or clustering Dimensionality
   Reduction Modeling Enables PCA SVM regression or neural networks 3 Methods of Conversion 3 1 Direct
   Coordinate Encoding Use raw coordinates as numeric features Example Latitude Longitude lat lon Suitable for
   points but limited for complex spatial objects polygons shapes 3 2 Distance Based Features Compute distances
   to reference points or landmarks Examples Distance to city center nearest river or road Distance to nearest
   hospital or facility for healthcare analytics Can be used in clustering classification or recommender systems
   3 3 Shape Based Features For polygons regions or irregular objects extract geometric descriptors Area Total
   region size Perimeter Length of the boundary Compactness Circularity 4 Area Perimeter24 pi times text Area
   text Perimeter 24 Area Perimeter2 Aspect ratio Width Height of bounding box Centroid coordinates Average
   position of all points in the shape Example Tumor shapes in medical images area perimeter elongation 3 4 Grid
   or Rasterization Convert spatial objects into grids or pixels Each grid cell can be numeric 0 empty 1 object
   present Or numeric intensity value e g elevation density Example GIS map 2D array of numeric values for each
   cell 3 5 Spatial Relationships Connectivity Features Encode relative positions of objects Examples Adjacency
   neighboring polygons Directional angles orientation Network distances roads rivers Useful for clustering and
   graph based learning 3 6 Statistical Features for Spatial Distributions Summarize patterns of points or
   objects in space Density Number of points per unit area Spatial variance Spread of points Centroid mean
   position Central tendency of objects 3 7 Embeddings for Spatial Graphs When spatial data is represented as a
   network graph Road networks utility networks or transportation graphs Use graph embedding algorithms Node2Vec
   GraphSAGE numeric vectors 4 Applications Geographic Information Systems GIS Predict land use urban planning
   Healthcare Analytics Tumor region features numeric inputs for disease detection Transportation Logistics
   Convert road networks into numeric vectors for route optimization Environmental Science Spatial patterns of
   rainfall pollution or vegetation numeric features for modeling Retail Marketing Customer location numeric
   features for targeted marketing 5 Advantages Limitations Method Advantages Limitations Coordinates Simple
   direct Limited for complex objects Distance Features Captures relative position Requires reference points
   Shape Features Captures geometry Ignores context with other objects Grid Rasterization Useful for images CNNs
   High dimensional sparse Spatial Graph Embeddings Captures relationships Requires graph preprocessing 6
   Summary Spatial data must be converted into numeric form to apply machine learning Techniques include Direct
   coordinates Distance based features Shape descriptors area perimeter aspect ratio Grid raster representations
   Statistical summaries of spatial distributions Graph embeddings for networks The choice of method depends on
   the complexity of spatial objects ML task and computational resources Graphs to Numeric Data 1 Introduction A
   graph G V E G V E G V E consists of nodes V and edges E that connect them Examples of graph data Social
   networks users as nodes friendships as edges Protein protein interaction networks Road networks and
   transportation graphs Citation networks Most machine learning algorithms require numeric feature vectors so
   graph data must be transformed into numeric representations while preserving the structure and relationships
   2 Why Convert Graphs to Numeric Compatibility Traditional ML algorithms SVM Random Forest Neural Networks
   cannot directly process nodes and edges Pattern Detection Capture node level edge level or graph level
   properties numerically Similarity Clustering Numeric vectors allow computation of distances or similarity
   between nodes graphs Predictive Modeling Node classification link prediction graph classification 3 Methods
   for Converting Graphs to Numeric Data 3 1 Node Level Features Generate numeric features for individual nodes
   based on graph topology Degree Number of edges connected to a node Clustering coefficient Measure of how
   connected the neighbors are Centrality measures Betweenness closeness eigenvector centrality PageRank
   Importance of a node in a network Example Social network node degree 5 clustering 0 3 betweenness 0 12 3 2
   Edge Level Features Generate numeric features for edges Weight of the edge if weighted Edge betweenness
   Similarity between connected nodes cosine similarity of node features 3 3 Graph Level Features Summarize the
   entire graph as a feature vector Number of nodes edges Density 2 E V V 1 Diameter longest shortest path
   Average clustering coefficient Graph motifs subgraph counts Useful for graph classification e g molecules
   protein structures 3 4 Adjacency or Laplacian Matrix Flattening Convert the adjacency matrix or graph
   Laplacian into a numeric vector flatten or use eigenvalues Pros Captures structure directly Cons High
   dimensional for large graphs 3 5 Graph Embedding Representation Learning Learn dense numeric embeddings of
   nodes or entire graphs using neural networks Node2Vec DeepWalk Random walks on the graph treat as sentences
   use Word2Vec to get node embeddings Graph Neural Networks GNNs Aggregate features from neighbors node level
   or graph level embeddings Examples GCN GraphSAGE GAT Graph level Embeddings Compute vector representations
   for entire graphs for graph classification tasks 3 6 Spectral Features Compute eigenvalues of the graph
   Laplacian or adjacency matrix Eigenvalues capture structural properties of the graph Can be used as numeric
   features for similarity clustering or classification 3 7 Kernel Based Methods Compute graph kernels to
   measure similarity between graphs Examples Shortest path kernel Random walk kernel Graphlet kernel The
   resulting kernel matrix is numeric and can be used in kernel based ML algorithms SVM 4 Applications Social
   Networks Node classification influence detection community detection Biology Protein or molecule
   classification drug discovery Transportation Route optimization traffic prediction Recommendation Systems
   User item bipartite graphs Cybersecurity Network intrusion detection using graph based features 5 Advantages
   Limitations Method Advantages Limitations Node level metrics Easy to compute interpretable May not capture
   global structure Edge level metrics Captures pairwise relationships Limited for node classification Graph
   level features Summarizes entire graph May lose node level details Adjacency Laplacian flattening Direct
   structure representation High dimensional for large graphs Embeddings Node2Vec GNN Captures structural
   semantic info Requires more computation data Spectral features Mathematically principled Sensitive to graph
   size noise Graph kernels Good for similarity based learning Computationally expensive 6 Summary Graphs must
   be converted to numeric features for machine learning tasks Approaches include Node edge and graph level
   metrics Adjacency or Laplacian matrix eigenvalues Graph embeddings Node2Vec GNNs Graph kernels Choice depends
   on graph size task node vs graph classification and computational resources Note From each student bring an
   example how to convert one data type to another Data Cleaning 1 Introduction Data Cleaning or data cleansing
   is the process of identifying and correcting errors or inconsistencies in datasets Real world data is often
   noisy incomplete inconsistent or redundant which can negatively affect model performance Cleaning ensures
   that machine learning models receive high quality reliable input leading to better predictions and insights 2
   Objectives of Data Cleaning Handle missing data Fill in gaps or remove incomplete records Correct incorrect
   entries Fix typos out of range values and inconsistencies Normalize data Ensure values are in a consistent
   scale or format Remove noise Detect and eliminate outliers or irrelevant information Ensure consistency
   Standardize naming units and categorical labels 3 Common Data Problems Problem Description Example Missing
   entries Data not recorded Age NULL Incorrect entries Typos invalid data Gender Mle instead of Male
   Inconsistent entries Different formats Date 2025 09 01 vs 09 01 2025 Outliers Values far from normal range
   Height 300 cm Redundancy Duplicate records Same customer entered twice Techniques in Data Cleaning Handling
   Missing Entries in Data Preprocessing 1 Introduction In real world datasets it is very common to find missing
   entries also called null values NA or NaN These occur when data is not recorded lost or unavailable Examples
   of missing data A customer doesn’t provide age or income in a survey A sensor fails to record a temperature
   reading A medical test result is unavailable for some patients If not handled properly missing data can lead
   to Biased results because the dataset no longer represents reality Reduced accuracy of machine learning
   models Errors when applying algorithms most models don’t accept NaN values 2 Types of Missing Data
   Understanding why data is missing is crucial before choosing a method to handle it MCAR Missing Completely at
   Random The missingness has no relationship with the data observed or unobserved Example Random technical
   glitch causes 5 of records to be missing MAR Missing at Random The missingness depends on observed data but
   not on the missing data itself Example Income is missing more often for younger respondents age observed
   income missing MNAR Missing Not at Random The missingness depends on the missing data itself Example People
   with very high income choose not to disclose their salary 3 Strategies for Handling Missing Data 3 1 Deletion
   Methods Listwise Deletion Remove any record row with missing values Works if only a small percentage of data
   is missing Risk Can reduce dataset size drastically Column Deletion Remove attributes columns with too many
   missing values Useful if 50 values are missing in a column 3 2 Imputation Methods Instead of deleting we fill
   in missing values with reasonable substitutes Simple Imputation Replace missing values with mean median or
   mode Example Missing age values replaced with the average age Hot Deck Imputation Replace missing values with
   observed values from similar records K Nearest Neighbors KNN Imputation Use the closest neighbors to estimate
   missing values Regression Imputation Predict missing values using regression models with other attributes
   Multiple Imputation Create several possible datasets with imputed values and combine results More
   statistically valid than single imputation 3 3 Using Domain Specific Knowledge Example In a medical dataset
   missing blood pressure may be imputed with clinically normal values if justified Example In time series data
   missing values can be filled using forward fill or interpolation Summary Handling missing entries ensures
   that datasets remain complete consistent and reliable Common strategies include deletion imputation mean
   median KNN regression and interpolation for time series The choice depends on the type of missingness and the
   importance of the data Scaling and Normalization 1 Introduction Scaling and normalization are techniques used
   to adjust the range or distribution of numeric data Machine learning algorithms often assume that features
   are on similar scales Without scaling Features with large numeric ranges can dominate distance based
   algorithms like KNN or SVM Gradient based algorithms like neural networks may converge slowly 2 Why Scale or
   Normalize Data Equal Importance Avoid bias towards features with larger values Faster Convergence Gradient
   descent converges faster when features are on similar scales Improved Accuracy Helps algorithms like KNN SVM
   PCA and clustering work better Compatibility Some methods require normalized input e g cosine similarity 3
   Common Methods 3 1 Min Max Scaling Normalization Rescales values to a fixed range usually 0 1 Formula x x
   xminxmax xminx frac x x min x max x min x xmax xmin x xmin Example Feature values 10 20 30 Min 10 Max 30
   Scaled 0 0 5 1 Pros Simple preserves relationships Cons Sensitive to outliers 3 2 Z Score Standardization
   Standard Scaling Centers the data at 0 and scales to unit variance Formula x x x frac x mu sigma x x Where mu
   mean of the feature sigma standard deviation Example Feature values 10 20 30 Mean 20 Std 8 16 Standardized 1
   22 0 1 22 Pros Less sensitive to outliers than min max Cons Does not bound values to a fixed range 3 3 Max
   Abs Scaling Scales values to 1 1 by dividing by the maximum absolute value x x xmax x frac x x max x xmax x
   Works well for data that is already centered at 0 3 4 Robust Scaling Uses median and IQR interquartile range
   to scale x x medianIQRx frac x text median text IQR x IQRx median Less sensitive to outliers 3 5 Decimal
   Scaling Move the decimal point of values to bring them into a specific range Formula x x10jwhere j is chosen
   such that x 1x frac x 10 j quad text where j is chosen such that x 1x 10jx where j is chosen such that x 1 4
   When to Use Which Method Method When to Use Notes Min Max Scaling Neural networks KNN SVM Sensitive to
   outliers Z Score Standardization Most ML models PCA clustering Handles outliers better Max Abs Scaling Sparse
   data e g text TF IDF vectors Preserves sparsity Robust Scaling Data with outliers Uses median IQR Decimal
   Scaling Simple scaling small datasets Rarely used in practice Data Reduction and Transformation 1
   Introduction Data Reduction The process of reducing the volume of data without losing important information
   Data Transformation Changing the format or representation of data to make it suitable for analysis or machine
   learning Together these steps help Reduce storage and computational requirements Improve efficiency of
   algorithms Enhance model accuracy by removing noise and redundant information 2 Objectives Reduce
   dimensionality number of features Reduce data size number of records Improve data quality and
   interpretability Prepare data for machine learning models 3 Techniques for Data Reduction 3 1 Sampling
   Definition Selecting a subset of data to represent the entire dataset Types Sampling for static data Randomly
   select a fixed number of rows Example Dataset has 1 000 000 records sample 10 100 000 records Reservoir
   sampling for data streams Maintain a fixed size sample from a stream of unknown length Useful when data
   cannot fit in memory Advantages Reduces computation speeds up analysis Disadvantages Risk of losing rare but
   important patterns 3 2 Feature Subset Selection Definition Selecting a subset of relevant features while
   removing irrelevant or redundant ones Methods Filter methods Evaluate features using statistical measures
   correlation chi square Wrapper methods Use ML algorithms to test feature subsets e g recursive feature
   elimination Embedded methods Feature selection is part of model training e g Lasso regression Advantages
   Reduces dimensionality improves model performance Disadvantages May require multiple trials or computation 3
   3 Dimensionality Reduction with Axis Rotation Transform high dimensional data into lower dimensions using
   mathematical techniques 3 3 1 Principal Component Analysis PCA Projects data onto orthogonal axes principal
   components capturing maximum variance Steps Standardize data Compute covariance matrix Compute eigenvectors
   and eigenvalues Select top k eigenvectors project data Applications Image compression visualization noise
   reduction 3 3 2 Singular Value Decomposition SVD Factorizes a matrix A U VTA U Sigma V TA U VT Reduces
   dimensionality while preserving key patterns Used in recommendation systems text mining and latent factor
   modeling 3 3 3 Latent Semantic Analysis LSA Special application of SVD in text mining Extracts hidden
   semantic structures from text document term matrix 3 4 Dimensionality Reduction with Type Transformation
   Transform data into a different representation to reduce dimensionality 3 4 1 Haar Wavelet Transform Converts
   data into wavelet coefficients representing both frequency and location Reduces dimensionality by discarding
   small coefficients Useful for time series image compression and denoising 3 4 2 Multidimensional Scaling MDS
   Maps high dimensional data into lower dimensions while preserving pairwise distances Useful for visualization
   and clustering 3 4 3 Spectral Transformation and Embedding of Graphs Converts graph data into numeric
   spectral embeddings using eigenvectors of Laplacian matrices Captures structural relationships in lower
   dimensional space 4 Advantages of Data Reduction and Transformation Technique Advantage Sampling Reduces data
   size speeds computation Feature Selection Removes irrelevant features improves accuracy PCA SVD LSA Reduces
   dimensions captures essential patterns Wavelet Transform Efficient compression noise reduction MDS Preserves
   distance relationships for visualization Spectral Graph Embedding Captures structural info in numeric vectors
   5 Applications Large scale datasets Sampling for faster analysis High dimensional datasets PCA SVD for
   dimensionality reduction Time series or image data Wavelet transforms Text mining NLP LSA for semantic
   analysis Graphs networks Spectral embedding for ML tasks 6 Summary Data Reduction and Transformation are
   essential to make datasets manageable efficient and suitable for ML Techniques include Sampling reduce number
   of records Feature selection reduce irrelevant features Axis rotation PCA SVD LSA reduce dimensions Type
   transformation Wavelets MDS spectral embeddings convert data to lower dimensional numeric form Proper
   reduction preserves important information while minimizing computational cost and noise Sampling in Data
   Science Definition Sampling
   + 2026 [3177–4193]:
      numerical input Suppose the categories are A B O One hot encoding creates one binary column for each
      category Patient P1 A 1 0 0 Patient P2 B 0 1 0 Patient P3 O 0 0 1 Here 1 category is present 0 category is
      absent Why Not Simply Use A 1 B 2 O 3 Using A 1 B 2 O 3 may incorrectly suggest that the categories have a
      numerical order For nominal categories such as blood type there is no meaningful order Therefore one hot
      encoding is usually more appropriate for nominal categorical data Text Data Numerical Data Text data
      includes Emails News articles Customer reviews Medical reports Social media posts Many numerical
      algorithms cannot directly process raw text Therefore text is converted into numerical features Example
      Document 1 good product Document 2 good service Vocabulary good product service Numerical representation
      D1 1 1 0 D2 1 0 1 Text Vectorization Common approaches include Bag of Words TF IDF Word embeddings
      Document embeddings General process Text Numerical Representation Machine Learning Data Mining The
      resulting representation may be a numerical vector such as 0 12 0 45 0 08 0 71 Time Series Numerical
      Features Sometimes we extract numerical characteristics from a time series Example process Original time
      series Feature extraction Mean standard deviation frequency features wavelet features Numerical vector The
      resulting numerical features can then be used by machine learning algorithms Time Series Symbolic Sequence
      A time series can also be represented using symbols For example Low A Medium B High C A numerical series
      such as 20 22 21 25 27 30 may become A A A B B C The numerical time series has been converted into a
      symbolic sequence Image Data Images are naturally represented using numerical values A grayscale image can
      be represented as a matrix of pixel intensities For example 0 25 80 120 10 40 100 150 20 60 130 200 For a
      grayscale image 0 Black 255 White A color RGB image normally contains three channels Red Green and Blue
      Image Numerical Features Instead of using every pixel useful features can be extracted Image Feature
      Extraction Shape Texture Edges Color Deep Features Numerical Vector The numerical vector can then be used
      by a classifier or clustering algorithm Spatial Data Spatial data describes objects according to their
      location Examples GPS coordinates Maps Geographic information Satellite data Locations of hospitals
      Example Hospital H1 Latitude 32 50 Longitude 45 82 Hospital H2 Latitude 32 48 Longitude 45 85 Spatial
      information can be transformed into numerical features that data mining algorithms can process Sequence
      Data A sequence is an ordered collection of elements Examples DNA A C G T A C G Customer actions Login
      Search Product Purchase Web navigation Home Products Laptop Checkout The order of elements is important
      Sequence data can sometimes be transformed into numerical features Graph Data A graph consists of Nodes
      vertices Edges connections Example A B C D A B C and D may represent users while the edges represent
      relationships Graph data can be transformed into numerical representations For example Node A 0 21 0 75 0
      43 Node B 0 19 0 81 0 39 Converting Different Data Types into a Graph Instead of converting everything
      into numerical data relationships between objects can be represented using a graph Suppose we have five
      patients If two patients are sufficiently similar we connect them The nodes represent objects and the
      edges represent similarity Similarity Graph A similarity graph can be created using a similarity or
      distance measure For example If distance P1 P2 threshold Connect P1 and P2 The graph represents which
      objects are similar to each other Applications Clustering Classification Nearest neighbor analysis Outlier
      detection General Data Type Portability Process Different data types can be transformed into
      representations suitable for analysis Numerical Discretization Categorical Encoding Text Vectorization
      Time Series Numerical Features or Symbolic Sequence Image Numerical Features Sequence Numerical Features
      Spatial Numerical Features Graph Numerical Representation The final representation is then provided to an
      appropriate data mining or machine learning algorithm Important Point Conversion Can Lose Information Data
      type conversion is useful but it may result in information loss Example Original ages 21 22 39 After
      discretization Adult Adult Adult The exact ages have disappeared Therefore A good conversion should
      preserve the important information needed for the mining task Advantages of Data Type Portability Data
      Type Portability can 1 Make heterogeneous data easier to process 2 Allow existing algorithms to work with
      different data types 3 Convert complex data into suitable representations 4 Facilitate integration of
      different data sources 5 Make machine learning and data mining algorithms easier to apply Limitations Data
      type conversion may have several limitations 1 Information loss 2 Loss of original structure 3 Possible
      distortion of relationships 4 High dimensional representations 5 Additional computational cost 6 The
      converted representation may not be suitable for every algorithm Therefore the conversion method should be
      selected according to the data and the mining task Data Conversion vs Data Mining Data Type Portability
      focuses on How can we represent data in a form suitable for an algorithm Data Mining focuses on How can we
      discover useful patterns or knowledge from the data Therefore Raw Data Data Preparation Data Type
      Conversion Mining Algorithm Patterns Prediction Knowledge Summary Data Type Portability is the process of
      converting data from one representation to another so that it can be processed by data mining algorithms
      Important examples Numerical Categorical Discretization Categorical Numerical One hot encoding Text
      Numerical TF IDF embeddings Time Series Numerical Feature extraction Time Series Sequence Symbolic
      representation Image Numerical Feature extraction Sequence Numerical Sequence encoding Graph Numerical
      Graph embedding Main idea Different data types require different representations Data Type Portability
      allows us to transform data into a representation that is more suitable for analysis and mining Quick
      Reference Table From To Example Technique Numerical Categorical Discretization Categorical Numerical One
      hot encoding Text Numerical TF IDF embeddings Time Series Numerical Feature extraction Time Series
      Sequence Symbolic representation Image Numerical Feature extraction Sequence Numerical Sequence encoding
      Graph Numerical Graph embedding Feature Selection Techniques in Data Mining Feature selection
7. − OLD [6213–6571]:
   a subset of data from a larger dataset called the population in such a way that the subset represents the
   whole dataset Instead of working with all data which may be too large costly or time consuming we use
   sampling to Reduce computational cost Speed up analysis Still capture the main patterns and distributions of
   the data Why Do We Use Sampling Efficiency Large datasets are expensive to process and store Scalability
   Algorithms may not work well on very large datasets Approximation A representative sample can provide similar
   insights as the full dataset Streaming Data In real time applications e g Twitter data sensor streams we
   cannot store everything Types of Sampling 1 Simple Random Sampling Each data point has an equal chance of
   being selected Example Picking 100 customers randomly from 1 million records 2 Stratified Sampling Data is
   divided into groups strata and samples are drawn from each group Ensures representation of all groups Example
   Sampling students by class year Freshman Sophomore Junior Senior 3 Systematic Sampling Select every k th item
   after a random start Example From a list of 10 000 customers select every 100th customer 4 Cluster Sampling
   Divide population into clusters randomly select some clusters and use all data within those clusters Example
   Selecting 3 cities randomly and surveying all households in them 5 Reservoir Sampling for data streams Useful
   when data arrives continuously streaming Maintains a representative sample of fixed size without knowing the
   total dataset size Example in Machine Learning Dataset 10 million rows of user transactions Training a model
   on all data is slow Use stratified random sampling to select 100 000 transactions while keeping the ratio of
   fraud vs non fraud cases Challenges in Sampling Bias If sampling is not random results may be skewed
   Representativeness Sample must reflect the population’s diversity Size Too small inaccurate too large
   inefficient In short Sampling is a data reduction technique where we take a representative portion of data to
   make computations easier and faster while still capturing the essential patterns of the entire dataset
   Feature Subset Selection 1 Introduction Feature Subset Selection is the process of choosing a subset of
   relevant features
   + 2026 [4199–4203]:
      the most relevant features attributes
8. − OLD [6580–6667]:
   ones Goal Improve model performance reduce overfitting and reduce computational cost Works best when datasets
   have high dimensional features such as text images or bioinformatics data 2 Why Feature Selection is
   Important Improves Model Accuracy Eliminates noisy or irrelevant features Reduces Overfitting Less redundant
   information means less chance for the model to learn noise Speeds Up Training Fewer features lower
   computational cost Enhances Interpretability Makes models easier to understand and explain Reduces Storage
   Requirements Smaller feature sets require less memory 3 Types of Feature Selection Methods 3 1
   + 2026 [4212–4357]:
      features For example if we want to predict whether a patient has diabetes the dataset may contain Age
      Glucose BMI Blood Pressure Insulin Skin Thickness Pregnancies Patient ID Some features may contribute
      strongly to prediction while others may provide little or no useful information Feature selection attempts
      to keep the useful features and remove the unnecessary ones Why is Feature Selection Important Feature
      selection can Reduce the number of features Remove irrelevant and redundant features Reduce computational
      cost Improve model performance in some cases Reduce the risk of overfitting Make the model easier to
      interpret Help visualize high dimensional data Main Feature Selection Techniques Feature selection
      techniques are commonly divided into three main categories Filter Methods Wrapper Methods Embedded Methods
      A simple way to remember them is Filter evaluate features Wrapper evaluate feature subsets using a model
      Embedded select features during model training 1 Filter Methods
9. − OLD [6674–7900]:
   statistical measures without involving any learning algorithm Independent of the model fast and scalable
   Common metrics Correlation Remove highly correlated features Chi square test For categorical features Mutual
   information Measures dependency between feature and target Variance thresholding Remove features with low
   variance Example Dataset Age Height Weight Zipcode Remove Zipcode if it has no correlation with the target 3
   2 Wrapper Methods Use a learning algorithm to evaluate feature subsets Select features that maximize model
   performance accuracy F1 score etc Methods Forward Selection Start with no features add features one by one
   Backward Elimination Start with all features remove one at a time Recursive Feature Elimination RFE
   Iteratively remove the least important feature using a model like SVM or Random Forest Pros Often more
   accurate than filter methods Cons Computationally expensive especially with many features 3 3 Embedded
   Methods Feature selection occurs naturally during model training Examples Lasso Regression L1 regularization
   Shrinks coefficients of less important features to zero Decision Trees Random Forests Feature importance
   scores can guide selection Gradient Boosting Machines Feature importance can be extracted from the model Pros
   Efficient considers interactions between features Cons Model dependent different models may select different
   features 4 Steps in Feature Subset Selection Understand the dataset Identify feature types numeric
   categorical ordinal Preprocess data Handle missing values scaling normalization Choose a selection method
   Filter wrapper or embedded Evaluate subsets Use cross validation or a validation set to measure model
   performance Select the final subset Retain features that maximize predictive power and minimize redundancy 5
   Practical Example Suppose we have a dataset for predicting diabetes with features Age BMI BloodPressure
   Glucose SkinThickness Insulin Pregnancies Filter method Compute correlation with target remove SkinThickness
   if correlation 0 1 Wrapper method Use RFE with Random Forest select Glucose BMI Age as most important
   features Embedded method Train Lasso regression coefficients of Insulin and Pregnancies shrink to zero remove
   them Final numeric feature vector for ML Glucose BMI Age 6 Advantages Limitations Method Type Advantages
   Limitations Filter Fast scalable Ignores feature interactions Wrapper Usually more accurate Computationally
   expensive Embedded Efficient considers interactions Model dependent 7 Summary Feature Subset Selection
   reduces dimensionality and improves model performance Techniques Filter methods Statistical relevance Wrapper
   methods Evaluate feature subsets with models Embedded methods Feature selection occurs during training Helps
   in avoiding overfitting improving interpretability and reducing computation Dimensionality Reduction with
   Axis Rotation 1 Introduction Dimensionality Reduction Process of reducing the number of features dimensions
   while retaining as much important information as possible Axis Rotation Transforming the coordinate system to
   align with the directions of maximum variance in the data This reduces redundancy and reveals underlying
   structure in the dataset 2 Why Axis Rotation Reduce Correlation Original features may be highly correlated
   rotation aligns axes along independent directions Compress Data Fewer dimensions needed to capture most of
   the variance Improve Visualization Easier to visualize data in 2D or 3D Enhance Model Performance Reduces
   noise and computational complexity 3 Techniques for Axis Rotation 3 1 Principal Component Analysis PCA Goal
   Find a new set of axes principal components that maximize the variance in the data Steps Standardize the data
   mean 0 variance 1 Compute the covariance matrix Compute eigenvectors directions and eigenvalues variance
   explained Sort eigenvectors by eigenvalues choose top k components Project data onto these principal
   components Example Original data 3 features X1 X2 X3 PCA 2 principal components PC1 PC2 Retain 95 of variance
   reduce dimension from 3 to 2 Pros Captures maximum variance Orthogonal components uncorrelated features Cons
   Linear method may not capture complex nonlinear patterns 3 2 Singular Value Decomposition SVD Factorizes the
   data matrix AAA into three matrices A U VTA U Sigma V TA U VT SVD provides an axis rotation similar to PCA
   Sigma contains singular values indicate importance of each axis Can reduce dimensions by keeping top k
   singular values and vectors Applications Text mining Latent Semantic Analysis Image compression 3 3 Other
   Axis Rotation Methods Factor Analysis Finds latent variables explaining correlations among observed features
   Independent Component Analysis ICA Rotates axes to achieve statistical independence of components Linear
   Discriminant Analysis LDA Axis rotation to maximize class separability supervised 4 Advantages Reduces
   dimensionality faster computation Removes redundancy uncorrelated features Retains maximum variance preserves
   important information Simplifies visualization and interpretation 5 Limitations PCA assumes linear
   relationships may miss nonlinear patterns Components are linear combinations may be hard to interpret
   Sensitive to scaling standardization is required 6 Applications Image Compression Reduce number of pixels
   while preserving most information Data Visualization Project high dimensional data to 2D or 3D Noise
   Reduction Remove dimensions with low variance assumed noise Preprocessing for Machine Learning Improve
   efficiency and performance Text Mining PCA or SVD reduces dimensionality of term document matrices 7 Summary
   Axis rotation transforms the feature space to orthogonal axes that capture maximum variance Main methods PCA
   Find uncorrelated principal components SVD Factorizes matrix to capture main directions ICA LDA Factor
   Analysis Other rotation based methods Axis rotation is a powerful tool for dimensionality reduction noise
   reduction and visualization Dimensionality Reduction with Type Transformation 1 Introduction Type
   Transformation involves converting data from one form or type to another while reducing dimensionality
   Instead of simply reducing the number of features along existing axes like PCA it changes the representation
   to extract essential information Useful for Time series data Image data Graph data Text data 2 Goals Reduce
   the number of features or variables Preserve important information in the transformed representation Make
   data suitable for machine learning algorithms Enable faster computation and efficient storage 3 Techniques 3
   1 Haar Wavelet Transform Wavelet transforms decompose data into different frequency components Haar wavelet
   simplest wavelet works by averaging and differencing adjacent values Steps Original data time series signal
   or image Apply Haar wavelet produces coefficients approximation details Keep top k coefficients reduces
   dimensionality Applications Time series compression Image compression and denoising Signal processing Example
   Signal 4 6 10 12 Haar transform Approximation 5 11 Detail 1 1 Use only 5 11 for compressed representation 3 2
   Multidimensional Scaling MDS Maps high dimensional data into lower dimensional space while preserving
   pairwise distances Steps Compute distance matrix between all points Find lower dimensional coordinates that
   best preserve distances Useful for visualization clustering and exploratory data analysis Applications
   Visualizing high dimensional datasets in 2D 3D Maintaining similarity relationships 3 3 Spectral
   Transformation and Graph Embedding Converts graph or network data into numeric vectors Steps Represent graph
   by adjacency or Laplacian matrix Compute eigenvectors captures structural relationships Select top k
   eigenvectors as numeric embedding Useful for Node classification Link prediction Graph based ML models 4
   Advantages Technique Advantages Haar Wavelet Captures both frequency location info compresses data
   efficiently MDS Preserves similarity between points good for visualization Spectral Graph Embedding Captures
   graph structure reduces dimensions for ML 5 Limitations Haar wavelet may lose fine details if coefficients
   discarded MDS computationally expensive for very large datasets Spectral embeddings require matrix
   computations sensitive to graph size 6 Applications Time series data Haar wavelet for compression and noise
   reduction Image processing Haar wavelet for denoising or compression Graph data Spectral embeddings for ML
   tasks High dimensional datasets MDS for visualization and clustering 7 Summary Type transformation reduces
   dimensionality by converting data into a different representation Key methods Haar Wavelet Transform captures
   frequency and location Multidimensional Scaling MDS preserves pairwise distances Spectral Transformation
   Graph Embedding numeric representation of graphs Benefits Reduces dimensions retains essential information
   enables efficient modeling and visualization
   + 2026 [4364–6161]:
      their statistical characteristics without using a data mining algorithm to evaluate the final feature
      subset They are usually fast and suitable for datasets with many features Common Filter Techniques 1 1
      Correlation Correlation measures the relationship between two variables For example Feature Correlation
      with Target Glucose 0 47 BMI 0 29 Age 0 24 Patient ID 0 01 Features with very weak relationships with the
      target may be removed Example If the correlation between Patient ID and diabetes is approximately 0
      Patient ID is probably not useful for prediction Important Low correlation does not always mean that a
      feature is useless because correlation mainly captures certain types of relationships especially linear
      relationships How to Calculate Correlation In data mining correlation measures the strength and direction
      of the relationship between two numerical variables The most commonly used measure is Pearson correlation
      coefficient denoted by 1 Pearson Correlation Formula Where value of variable value of variable mean of
      mean of number of observations correlation coefficient 2 Simple Example Suppose we have Age and Blood
      Pressure for five people Person Age X Blood Pressure Y 1 20 110 2 30 120 3 40 130 4 50 140 5 60 150 Step 1
      Calculate the means Step 2 Calculate deviations X Y 20 110 20 20 30 120 10 10 40 130 0 0 50 140 10 10 60
      150 20 20 Step 3 Calculate the products Therefore Step 4 Calculate squared deviations Similarly Step 5
      Calculate So the correlation is This means there is a perfect positive linear correlation between Age and
      Blood Pressure in this example 1 2 Chi Square Test The Chi square test measures the relationship between
      categorical features and a categorical target For example Smoking Status Heart Disease A high Chi square
      statistic indicates a stronger association between the feature and the target It is commonly used for
      classification problems with categorical or non negative discrete features Example Suppose we want to
      predict whether a person has Heart Disease based on Smoking Status We have Heart Disease Yes Heart Disease
      No Total Smoker 40 20 60 Non Smoker 20 70 90 Total 60 90 150 The Chi Square test compares Observed
      frequencies what we actually see in the dataset Expected frequencies what we would expect if Smoking
      Status and Heart Disease were independent Hypotheses The Chi Square test uses two hypotheses Null
      hypothesis The feature and the target are independent In our example Smoking Status is not associated with
      Heart Disease Alternative hypothesis The feature and the target are associated In our example Smoking
      Status is associated with Heart Disease Calculate Expected Frequencies The expected frequency is
      calculated as For Smoker Heart Disease Yes For Smoker Heart Disease No For Non Smoker Heart Disease Yes
      For Non Smoker Heart Disease No Therefore Disease Yes Disease No Smoker Observed 40 Observed 20 Expected
      24 Expected 36 Non Smoker Observed 20 Observed 70 Expected 36 Expected 54 Calculate Chi Square Statistic
      The formula is where Observed frequency Expected frequency For our example Therefore A relatively large
      Chi Square value indicates that the observed frequencies differ substantially from what would be expected
      if the variables were independent What Does the Chi Square Value Mean A larger Chi Square statistic
      generally indicates stronger evidence of an association between the feature and target However when using
      Chi Square for feature selection it is often more convenient to look at the p value For a table Therefore
      We then use the Chi Square distribution to obtain the p value If we commonly reject and conclude that
      there is statistical evidence of an association between the feature and target 1 3 Information Gain
      Information Gain measures how much information a feature provides about the target A feature that
      significantly reduces uncertainty about the target has high information gain For example Feature A
      Information Gain 0 42 Feature B Information Gain 0 08 Feature A would generally be considered more
      informative than Feature B Information Gain is commonly associated with decision tree based feature
      selection Information Gain for Feature Selection Simple Example Suppose we want to predict whether a
      student will Pass or Fail We have 8 students Student Attendance Study Hours Result 1 High High Pass 2 High
      High Pass 3 High Low Pass 4 High Low Fail 5 Low High Pass 6 Low Low Fail 7 Low Low Fail 8 Low High Fail We
      want to answer Which feature is more useful for predicting the Result Attendance or Study Hours Step 1
      Calculate the initial Entropy There are Pass 4 Fail 4 Therefore So Step 2 Calculate Information Gain for
      Attendance Attendance has two groups High Attendance Students 1 4 Result Number Pass 3 Fail 1 Entropy Low
      Attendance Students 5 8 Result Number Pass 1 Fail 3 Therefore Weighted Entropy Each group contains 4 out
      of 8 students Information Gain Step 3 Calculate Information Gain for Study Hours High Study Hours Students
      1 2 5 8 Result Number Pass 3 Fail 1 Therefore Low Study Hours Students 3 4 6 7 Result Number Pass 1 Fail 3
      Therefore Weighted Entropy Information Gain Step 4 Compare Them Feature Information Gain Attendance 0 189
      Study Hours 0 189 In this particular dataset both features have the same Information Gain Therefore based
      only on Information Gain Attendance and Study Hours provide the same amount of information about the
      student's result The basic process to teach students Attendance Information Gain 0 189 Compare Study Hours
      Information Gain 0 189 The general rule is So if Attendance had an Information Gain of 0 35 and Study
      Hours had 0 12 we would select Attendance as the more informative feature 1 4 Mutual Information Mutual
      Information MI measures the amount of information shared between a feature and the target It can capture
      nonlinear relationships which makes it different from simple correlation For example If Feature X has a
      nonlinear relationship with the target correlation might be low while mutual information may still be high
      The main equation for Mutual Information MI is Where the feature the target uncertainty entropy of the
      target before knowing the feature uncertainty of the target after knowing the feature Information Gain How
      much does the feature reduce the uncertainty of the target Mutual Information How much information does
      the feature and target share Example Suppose we want to predict whether a student will Pass or Fail We
      have two features Attendance Study Hours Dataset Student Attendance Study Hours Result 1 High High Pass 2
      High Low Pass 3 High High Pass 4 High Low Pass 5 Low High Fail 6 Low Low Fail 7 Low Low Fail 8 Low High
      Fail Notice that Attendance perfectly separates the two classes High Pass Low Fail But Study Hours does
      not High sometimes Pass sometimes Fail Low sometimes Pass sometimes Fail 1 Mutual Information of
      Attendance Before using Attendance Pass 4 Fail 4 Therefore After knowing Attendance Attendance High All 4
      students Pass Attendance Low All 4 students Fail Therefore So 2 Mutual Information of Study Hours Now
      consider Study Hours Study Hours High Students Student Result 1 Pass 3 Pass 5 Fail 8 Fail So Pass 2 Fail 2
      Therefore Study Hours Low Students Student Result 2 Pass 4 Pass 6 Fail 7 Fail Again Pass 2 Fail 2
      Therefore Thus and 3 Compare the Two Features Feature Mutual Information Attendance 1 0 Study Hours 0 0
      Therefore Why Attendance completely determines the result in this example High attendance Pass Low
      attendance Fail But Study Hours provides no useful information here because both High and Low study hours
      contain an equal number of Pass and Fail students 1 5 Variance Threshold This method removes features with
      very low variance If a feature has almost the same value for every observation it provides little
      information for distinguishing observations Example Patient Feature 1 1 2 1 3 1 4 1 5 1 This feature has
      zero variance and can usually be removed 2 Wrapper Methods Wrapper methods use a data mining or machine
      learning algorithm to evaluate different subsets of features Instead of evaluating features individually
      they ask Which combination of features produces the best model performance Common Wrapper Techniques 2 1
      Forward Selection Starts with no features Then Add the feature that improves performance the most Add
      another feature that provides the next largest improvement Continue until a stopping condition is reached
      Example Start No features Add Glucose Add BMI Add Age Add Blood Pressure Final subset 2 2 Backward
      Elimination Starts with all features Then Train the model using all features Remove the least useful
      feature Retrain the model Continue removing features Example All features Remove Patient ID Remove Skin
      Thickness Remove Insulin Final subset 2 3 Recursive Feature Elimination RFE RFE repeatedly trains a model
      and removes the least important features For example 10 features Train model Remove least important
      feature 9 features Train model Remove least important feature 5 selected features RFE can be used with
      algorithms such as Logistic Regression SVM and Random Forest depending on the implementation 3 Embedded
      Methods Embedded methods perform feature selection during the model training process Therefore feature
      selection is part of the learning algorithm itself Common Embedded Techniques 3 1 LASSO Regression LASSO
      uses L1 regularization It adds a penalty to the model The L1 penalty can force some coefficients to become
      exactly zero For example Feature Coefficient Glucose 0 82 BMI 0 31 Age 0 15 Insulin 0 Patient ID 0
      Features with coefficients equal to zero can be removed 3 2 Decision Trees Decision trees select features
      when constructing the tree For example Glucose High Low BMI Age The tree gives greater importance to
      features that provide useful splits Feature importance can then be used for feature selection 3 3 Random
      Forest Feature Importance Random Forest can calculate feature importance based on how much features
      contribute to reducing impurity or depending on the method how much they affect prediction performance
      Example Feature Importance Glucose 0 31 BMI 0 18 Age 0 14 Blood Pressure 0 09 Patient ID 0 00 Features
      with very low importance may be removed Comparison of the Three Main Methods Method Basic Idea Model
      Required Speed Filter Evaluate features using statistical measures No Fast Wrapper Evaluate feature
      subsets using a model Yes Slow Embedded Select features during model training Yes Medium Fast Simple
      Example Suppose we have 20 features and want to select the most useful ones Filter Calculate statistical
      scores select top 8 features Wrapper Try different combinations train model choose the subset producing
      the best performance Embedded Train a model model automatically assigns zeros feature coefficients or
      importance select important features Key Difference Filter methods select features before model training
      Wrapper methods select features by repeatedly evaluating a model Embedded methods select features as part
      of model training

## Association pattern mining

**المصادر القديمة:** DM_Association_Pattern_Mining (archive).docx.  **مصادر 2026:** Week5.docx.

**الكلمات المرمّزة:** القديم 3,628؛ الحالي 3,554؛ المتطابق بالترتيب 948. Direct title and section mapping.

1. − OLD [5–115]:
   rules offer a powerful tool for data analysis providing insights into patterns and relationships within large
   datasets While they are a staple in market basket analysis their application extends across various domains
   offering invaluable insights into customer behaviour and beyond Introduction to Association Rules in Data
   Mining Association rule mining is a technique in data mining for discovering interesting relationships
   frequent patterns associations or correlations between variables in large datasets It’s widely used in
   various fields such as market basket analysis web usage mining bioinformatics and more The basic idea is to
   find rules that predict the occurrence of an item based on the occurrences of other items in the transaction
   + 2026 [5–106]:
      Pattern Mining is a data mining technique used to discover interesting relationships associations or co
      occurrence patterns among items in a dataset In simple words It finds items or events that frequently
      occur together and identifies useful relationships between them Main concepts Association pattern mining
      generally involves Items individual elements such as Bread Milk Coffee Itemsets collections of items such
      as Bread Milk Frequent Itemsets itemsets that occur frequently enough according to a minimum support
      threshold Association Rules relationships expressed as Support how frequently the combination occurs
      Confidence how often occurs when occurs Lift how strongly and are associated compared with independence
   + 2026 [166–189]:
      Transaction Items Purchased T1 Bread Milk Butter T2 Bread Diaper Coffee T3 Milk Diaper Coffee T4 Bread
      Milk Diaper T5 Bread Milk Diaper Coffee
3. − OLD [265–265]:
   Beer
   + 2026 [280–280]:
      Coffee
4. − OLD [275–275]:
   Beer
   + 2026 [290–290]:
      Coffee
5. − OLD [285–285]:
   Beer
   + 2026 [300–300]:
      Coffee
6. − OLD [378–418]:
   Market Basket Analysis This is a primary application of association rules focusing on analyzing purchase
   patterns By examining combinations of items that frequently occur together in purchases businesses can gain
   insights into marketing and sales strategies Figure 2 Market Basket Analysis
7. − OLD [428–428]:
   BEER
   + 2026 [402–402]:
      COFFEE
8. − OLD [540–614]:
   The strength and reliability of an association rule are measured using three key metrics Association rule
   mesures Support These measure how frequently the item both X and Y together appears in the dataset It’s the
   proportion of transactions that contain both X and Y to all transactions High support indicates that the
   items are common in transactions Confidence This measures the likelihood of finding the consequence in
   transactions under the condition that these transactions also
   + 2026 [514–607]:
      After generating association rules we need to determine how strong and useful each rule is Three key
      measures are used to evaluate association rules Support Confidence Lift Consider the rule 1 Support
      Support measures how frequently the antecedent and consequent occur together in the entire transaction
      database where antecedent consequent total number of transactions Example Suppose Bread and Milk occur
      together in 3 out of 5 transactions Therefore Support 60 A high support means that the combination occurs
      frequently in the dataset 2 Confidence Confidence measures how often the consequent occurs in transactions
      that
9. − OLD [620–664]:
   in a rule like Bread Butter the confidence measures how often butter is bought when bread is bought Lift
   These measures show how much more often the antecedent and consequence of the rule occur together than we
   would expect if they were statistically independent This
   + 2026 [613–645]:
      suppose Bread appears in 4 transactions Bread and Milk appear together in 3 transactions Then Therefore
      Confidence 75 This means that 75 of the transactions containing Bread also contain Milk 3 Lift Lift
10. − OLD [672–1278]:
   X and Y A lift value greater than 1 implies that the antecedent and consequent are dependent Lift evaluates
   the strength of the rule over the randomness A lift greater than 1 indicates a strong rule Lift 1 Positive
   association X increases chance of Y Lift 1 Independent Lift 1 Negative association X decreases chance of Y
   Association Rules A Step by Step Example Now let’s derive some potential association rules from Table 1 data
   Imagine a dataset of customer purchases from a grocery store Each transaction is a record of different items
   bought together By applying association rules we can discover patterns like customers who buy Tea often also
   buy Honey Example 01 Rule Bread Milk Interpretation Customers who buy Bread are likely to buy Milk as well
   Support Calculated the number of transactions containing both Bread and Milk divided by the total number of
   transactions Identify Transactions Containing Both Bread and Milk o T1 Milk Bread Butter o T4 Bread Milk
   Diapers Beer o T5 Bread Milk Diapers Cola Here 3 out of 5 transactions contain both Bread and Milk Calculate
   Support Support 3 transactions with both items 5 total transactions 0 6 or 60 Confidence The number of
   transactions with both Bread and Milk divided by the number of transactions with just Bread Identify
   Transactions Containing Bread T1 T2 T4 T5 4 transactions contain Bread Calculate Confidence Confidence 3
   transactions with both Bread and Milk 4 transactions with Bread 0 75 or 75 This calculation shows that not
   only is the combination of Bread and Milk common in this dataset but also that there’s a high likelihood of
   Milk being purchased when Bread is bought Example 02 Rule Diapers Beer Milk Interpretation Customers who buy
   Diapers and Beer together are likely to buy Milk too Support The support for this rule is 0 4 meaning that
   Diapers Beer and Milk are bought together in 40 of all transactions This is calculated by dividing the number
   of transactions that include all three items Diapers Beer and Milk by the total number of transactions
   Confidence The confidence for this rule is approximately 0 67 or 66 67 indicating that in about 67 of the
   transactions where Diapers and Beer are bought Milk is also purchased This is calculated by dividing the
   number of transactions that include all three items by the number of transactions that include just Diapers
   and Beer Example 03 Rule Milk Bread Diapers Interpretation Customers who buy Milk and Bread are likely to buy
   Diapers Support The support for this rule is also 0 4 which means that Milk Bread and Diapers are purchased
   together in 40 of all transactions This is computed in the same way as above considering the transactions
   that include Milk Bread and Diapers Confidence The confidence for this rule is also about 0 67 suggesting
   that in approximately 67 of the transactions where Milk and Bread are bought Diapers are also purchased This
   is found by dividing the number of transactions with all three items Milk Bread and Diapers by the number of
   transactions with just Milk and Bread Note In this example we would calculate the support and confidence for
   each rule to determine their strength and relevance It’s important to note that these are just hypothetical
   rules Actual analysis may require more complex algorithms like Apriori or FP Growth and consideration of
   additional factors like lift Practical Applications Market Basket Analysis Understanding customer purchasing
   patterns like finding that customers who buy pasta also often buy tomato sauce Retail Insights Identifying
   products that are often purchased together to optimize store layout or promotions Cross Selling Strategies
   Suggesting
   + 2026 [653–893]:
      the antecedent and consequent by comparing their actual co occurrence with the co occurrence expected if
      they were independent Interpretation Lift Meaning Lift 1 Positive association Lift 1 No association
      independence Lift 1 Negative association For example if this indicates that Bread and Milk occur together
      more often than would be expected if they were independent Summary Measure Main Question Support How
      frequently do X and Y occur together Confidence When X occurs how often does Y occur Lift How strong is
      the association between X and Y compared with independence Important Note These measures describe
      association not causation For example does not mean that buying Bread causes a customer to buy Milk It
      only indicates that the two items occur together according to the observed transaction data Your lecture
      also emphasizes this non causality point Practical Applications of Association Rule Mining Association
      rule mining can be applied in many areas to discover useful relationships and patterns among items or
      events The main applications presented in your lecture are the following 1 Market Basket Analysis
      Association rules are widely used in retail to discover products that customers frequently purchase
      together Example A supermarket can use such patterns to understand customer purchasing behavior 2 Retail
      Insights Retailers can identify products that are frequently purchased together and use this information
      to Improve store layout Design product promotions Organize product placement Understand customer
      purchasing patterns 3 Cross Selling Association rules can help businesses recommend
11. − OLD [1288–1378]:
   Healthcare and Research In medical research association rules can help in identifying correlations between
   different symptoms or drug interactions Fraud Detection Identifying patterns in transactions that might
   indicate fraudulent activity Recommendation Systems Enhancing customer experience by recommending relevant
   items For example online streaming services recommend movies based on viewing history Critical Considerations
   Non causality It’s crucial to remember that these rules indicate correlation not causation They highlight
   patterns of co occurrence not the reasons behind them Domain Knowledge To derive meaningful conclusions
   domain expertise is essential to interpret these patterns correctly
   + 2026 [903–1065]:
      Example If a customer purchases and many similar transactions also contain the system may recommend a
      Mouse to that customer 4 Healthcare and Research Association mining can be used to discover relationships
      among Symptoms Diseases Treatments Medications Patient characteristics For example researchers may
      discover that certain symptoms frequently occur together in a particular group of patients Important Such
      a rule indicates an association and does not by itself establish a causal relationship 5 Fraud Detection
      Association patterns can help identify unusual combinations or patterns in financial transactions that may
      be associated with fraudulent activity For example a system may identify unusual combinations of
      Transaction amount Location Time Transaction type and flag them for further investigation 6 Recommendation
      Systems Association rules can be used to recommend items based on items that a user has already selected
      or interacted with For example A customer watches Movie A and Movie B recommend Movie C Similarly online
      stores can recommend products based on products frequently purchased together
12. − OLD [1384–1492]:
   Large Number of Rules Even with a small number of items the potential number of rules can be vast many of
   which may not be useful Setting Thresholds Determining the right support and confidence thresholds requires
   domain knowledge and can significantly impact the quality of the generated rules Interpretation and
   Actionability Not all discovered rules are useful or actionable Some might be trivial or require further
   investigation to understand their practical implications Frequent Itemset Generation Continuing from the
   discussion on association rules and their classifications let’s delve deeper into the concept of frequent
   itemset generation a crucial step in mining association rules Understanding Frequent Itemset Frequent Itemset
   These are
   + 2026 [1071–1539]:
      Association rule mining can face several challenges when working with real world datasets The number of
      possible item combinations can become very large as the number of items increases A mining algorithm may
      generate a very large number of rules making it difficult to identify the most useful ones Choosing
      suitable minimum support and minimum confidence values can be difficult Very high values may remove useful
      rules while very low values may generate too many rules Mining large datasets can require considerable
      processing time and memory Some discovered rules may be redundant obvious or uninteresting even if they
      satisfy the required thresholds Important patterns may occur rarely A high minimum support threshold can
      therefore remove some potentially valuable patterns A statistically strong rule is not necessarily useful
      in practice Domain knowledge may be needed to determine whether a rule has practical value Association
      rules show relationships not causation A rule does not prove that one item causes another item to occur
      Poor quality data such as missing incorrect duplicated or inconsistent data can lead to misleading rules
      Patterns can change over time because customer behavior products and market conditions change Therefore
      rules discovered from old data may not remain useful Frequent Itemset Generation Frequent Itemset
      Generation is the process of finding groups of items that occur together frequently in a transaction
      database An itemset is considered frequent when its support is greater than or equal to a predefined
      minimum support min sup threshold Minimum support min sup is a user defined threshold that determines how
      frequently an itemset must occur in a dataset to be considered a frequent itemset Simple Example Suppose
      we have these transactions Transaction Items T1 Bread Milk T2 Bread Coffee T3 Bread Milk Coffee T4 Milk
      Coffee T5 Bread Milk Suppose There are 5 transactions so an itemset must appear in at least transactions
      Therefore Bread 4 transactions Frequent Milk 4 transactions Frequent Coffee 3 transactions Frequent Bread
      Milk 3 transactions Frequent Bread Coffee 2 transactions Frequent Milk Coffee 2 transactions Frequent
      Bread Milk Coffee 1 transaction Not frequent So the frequent itemsets are the itemsets whose support
      satisfies the minimum support threshold Why is it important Frequent itemset generation is usually the
      first major step in association rule mining For example after discovering the frequent itemset Bread Milk
      Coffee we can generate rules such as Bread Milk Coffee or Bread Milk Coffee and then evaluate these rules
      using confidence lift and other measures Common approaches Several algorithms can be used to generate
      frequent itemsets including Brute Force Apriori FP Growth ECLAT The main challenge is that the number of
      possible itemsets grows exponentially as the number of items increases Therefore algorithms such as
      Apriori and FP Growth use strategies to reduce the amount of unnecessary searching In simple terms
      Frequent itemset generation means finding
13. − OLD [1498–1545]:
   frequently in your dataset The frequency is determined based on a user defined threshold known as the support
   threshold Support Threshold This is a critical parameter that helps in identifying items that are significant
   for analysis It’s a percentage indicating how often an item should appear in the
   + 2026 [1545–1549]:
      together often enough in a
14. − OLD [1551–1690]:
   Example of Frequent Itemset Let’s return to our grocery store example Suppose we set a support threshold of
   50 An item set like Milk Bread might be considered frequent if it appears in 50 or more of the transactions
   Significance of Frequent Itemset Filtering Out Noise By focusing on frequent item sets we can ignore item
   combinations that occur rarely and are likely insignificant or coincidental Efficiency This approach greatly
   reduces computational complexity by limiting the number of item sets and association rules we need to
   consider Calculating Support Support Calculation The support of an itemset is calculated as the number of
   transactions in which the item set appears divided by the total number of transactions Example Calculation If
   there are 100 transactions and Milk Bread appears in 40 of them the support is 40 100 0 4 or 40
   + 2026 [1555–1650]:
      Frequent Itemset Generation vs Association Pattern Mining These two concepts are related but not the same
      Aspect Frequent Itemset Generation Association Pattern Mining Meaning Finds groups of items that occur
      frequently together Discovers useful relationships and patterns among items Main goal Identify frequent
      itemsets Discover association rules and patterns Output Frequent itemsets Association rules and other
      patterns Example Bread Milk occurs frequently Bread Milk Main measure Support Support Confidence Lift etc
      Algorithms Apriori FP Growth ECLAT Association rule generation using frequent itemsets and rule measures
      Position Usually a step within association mining Broader data mining task
15. − OLD [1738–1739]:
   1 Definition
   + 2026 [1698–1700]:
      Brute Force Algorithm
16. − OLD [1746–2027]:
   na ve approach to frequent itemset generation It simply enumerates all possible itemsets and checks whether
   each one is frequent For nnn items there are 2n 1 possible itemsets For each candidate itemset it scans the
   dataset to count its support Finally it selects the itemsets whose support min sup 2 Steps Generate all
   subsets of items 2n 1 For each subset scan the database and count how many transactions contain it Keep only
   those itemsets that satisfy minimum support From frequent itemsets generate association rules and test
   confidence min conf 3 Example Dataset 5 transactions TID Items 1 Bread Milk 2 Bread Diaper Beer 3 Milk Diaper
   Beer 4 Bread Milk Diaper 5 Bread Milk Diaper Beer Items Bread Milk Diaper Beer so possible subsets 24 1 16 1
   15 The brute force method would Check support for each Bread Milk Diaper Beer Bread Milk Bread Milk Diaper
   Beer Keep those min sup say 0 6 This requires 15 5 75 checks just for 4 items Imagine if there were 100 items
   21002 100 2100 itemsets impossible 4 Advantages Simple easy to understand Guarantees to find all frequent
   itemsets no approximation 5 Disadvantages Exponential time complexity O N 2n where N number of transactions n
   number of items Not scalable for large datasets Motivates better algorithms like Apriori FP Growth and ECLAT
   In short The Brute Force Algorithm is the most basic method for frequent itemset generation generate all
   possible itemsets scan dataset and select frequent ones While it works for small datasets it is too slow for
   large real world data which is why Apriori and FP Growth were developed Apriori Algorithm 1 Definition The
   Apriori Algorithm is an iterative
   + 2026 [1707–1943]:
      simplest approach for frequent itemset generation It examines all possible non empty itemsets and
      determines whether each one satisfies the minimum support threshold If a dataset contains different items
      the total number of possible non empty itemsets is How it works The algorithm follows these basic steps
      Generate all possible itemsets from the available items Calculate the support of each itemset by scanning
      the transaction database Compare the support of each itemset with the minimum support min sup Keep the
      itemsets whose support is greater than or equal to min sup Use the resulting frequent itemsets to generate
      association rules Simple Example Suppose we have four items The number of possible non empty itemsets is
      These include 1 itemsets 2 itemsets 3 itemsets 4 itemset The algorithm checks the support of all 15
      itemsets and keeps only those satisfying the minimum support threshold Main Advantage The main advantage
      is its simplicity It is easy to understand and for a small dataset can find all frequent itemsets Main
      Disadvantage The major problem is high computational cost The number of possible itemsets increases
      exponentially as the number of items increases For example but which is an extremely large number
      Therefore brute force is generally practical only for small datasets or a small number of items Its
      limitations motivate more efficient approaches such as Apriori and FP Growth Apriori Algorithm Apriori
      Algorithm The Apriori Algorithm is a frequent itemset mining
17. − OLD [2036–2044]:
   transactional database It is based on the Apriori property
   + 2026 [1952–1988]:
      transaction database and then generate association rules from them The main idea behind Apriori is to
      reduce the number of itemsets that need to be examined by using the Apriori property Apriori Property The
      Apriori property states
18. − OLD [2050–2053]:
   then all of its
   + 2026 [1994–1998]:
      all of its non empty
19. − OLD [2059–2063]:
   If an itemset is infrequent
   + 2026 [2004–2010]:
      Equivalently If an itemset is not frequent
20. − OLD [2071–2090]:
   This property allows the algorithm to prune the search space and avoid brute force enumeration 2 Steps of
   Apriori Algorithm
   + 2026 [2018–2050]:
      For example if is not frequent then cannot be frequent either Therefore there is no need to calculate the
      support of the larger itemset How Apriori Works The algorithm works level by level
21. − OLD [2097–2439]:
   C1 Count the support of each item Keep those meeting min sup Frequent 1 itemsets L1 Step 2 Generate Candidate
   k itemsets Ck Join frequent k 1 itemsets to form k itemsets Example From Bread Milk Diaper we get Bread Milk
   Bread Diaper Milk Diaper Step 3 Prune Remove itemsets that have infrequent subsets Example If Bread Beer is
   infrequent then Bread Milk Beer is automatically removed Step 4 Count Support Scan the database to count how
   many transactions contain each candidate itemset Step 5 Select Frequent Itemsets Keep only those itemsets
   whose support min sup Step 6 Repeat Repeat steps 2 5 until no new frequent itemsets are found Step 7 Generate
   Association Rules From frequent itemsets create rules X Y Keep only rules with confidence min conf 3 Example
   Dataset 5 transactions TID Items 1 Bread Milk 2 Bread Diaper Beer 3 Milk Diaper Beer 4 Bread Milk Diaper 5
   Bread Milk Diaper Beer Let min sup 0 6 3 5 L1 Frequent 1 itemsets Bread 4 Milk 4 Diaper 4 Beer 3 L2 Frequent
   2 itemsets Bread Milk 3 Bread Diaper 3 Milk Diaper 3 Milk Beer 2 Bread Beer 2 Diaper Beer 3 L3 Frequent 3
   itemsets Bread Milk Diaper 3 Bread Milk Beer 2 Milk Diaper Beer 2 Bread Diaper Beer 2 L4 Frequent 4 itemsets
   Bread Milk Diaper Beer 2 stop Frequent Itemsets Bread Milk Diaper Diaper Beer etc From these rules like Bread
   Milk support 0 6 confidence 0 75 Diaper Beer support 0 6 confidence 0 75 4 Advantages More efficient than
   brute force prunes search space Widely used and easy to implement Guarantees correct results 5 Disadvantages
   Still requires multiple scans of the database Generates too many candidate itemsets in large datasets Not as
   fast as FP Growth In summary The Apriori Algorithm finds frequent itemsets using the downward closure
   property Apriori property It reduces search space by pruning infrequent itemsets early making it much better
   than brute force but for very large datasets FP Growth is faster The FP Growth Algorithm 1 Introduction
   + 2026 [2057–2345]:
      Find all individual items in the database and calculate their support Step 2 Find frequent 1 itemsets Keep
      only the items whose support satisfies Step 3 Generate candidate 2 itemsets Combine the frequent 1
      itemsets to create possible pairs Step 4 Prune Remove candidates that contain an infrequent subset Step 5
      Calculate support Count how frequently the remaining candidates occur Step 6 Find Keep candidates that
      satisfy min sup The same process continues for and so on until no more frequent itemsets can be generated
      Simple Example Consider five transactions Transaction Items T1 Bread Milk T2 Bread Coffee T3 Bread Milk
      Coffee T4 Milk Coffee T5 Bread Milk Suppose Since there are five transactions an itemset must appear in at
      least 2 transactions Step 1 Find The individual items are Bread 4 transactions 80 Milk 4 transactions 80
      Coffee 3 transactions 60 Therefore All three are frequent Step 2 Generate From generate Their supports are
      Bread Milk 3 5 60 Bread Coffee 2 5 40 Milk Coffee 2 5 40 All satisfy the 40 minimum support Therefore Step
      3 Generate The possible 3 itemset is It appears only in T3 Since it is not frequent Therefore the
      algorithm stops Why is Apriori Better Than Brute Force Brute Force generates and tests every possible
      itemset Apriori uses the Apriori property to prune impossible candidates early Therefore Apriori reduces
      the search space by eliminating itemsets that cannot possibly be frequent However Apriori can still become
      expensive for very large datasets because it may generate many candidates and repeatedly scan the database
      In simple terms Apriori finds frequent itemsets level by level using the principle that an infrequent
      itemset cannot have a frequent superset The FP Growth Algorithm The FP Growth Algorithm
22. − OLD [2448–2512]:
   a frequent itemset mining algorithm used in data mining particularly for association rule learning It’s an
   efficient alternative to the Apriori algorithm especially when the dataset is large Goal To find frequent
   itemsets in a transaction database without generating candidate itemsets explicitly 2 Key Concepts Frequent
   Itemset A set of items that appears together in transactions more than a user defined threshold called
   minimum support
   + 2026 [2354–2409]:
      an efficient algorithm for frequent itemset generation It was developed to overcome some of the
      limitations of the Apriori algorithm particularly the need to generate and test a large number of
      candidate itemsets The main idea is FP Growth finds frequent itemsets without explicitly generating
      candidate itemsets Instead it uses a compact data structure called an
23. − OLD [2518–2598]:
   A compact tree structure that stores quantitative information about frequent patterns Each node represents an
   item and its count 3 Advantages Over Apriori Feature FP Growth Apriori Candidate Generation None Generates
   many candidates Database Scans 2 Multiple times Efficiency High for large datasets Slower for large datasets
   Memory Usage Compact FP tree Larger memory for candidates 4 Steps of FP Growth Algorithm Step 1 Scan Database
   Find Frequent Items Scan the transaction database to find items that satisfy minimum support Sort
   + 2026 [2415–2451]:
      to represent the transaction database How FP Growth Works The algorithm generally follows these steps Scan
      the database and calculate the frequency of each item Remove infrequent items that do not satisfy min sup
      Sort the remaining
24. − OLD [2604–2782]:
   frequency Step 2 Build FP Tree Create a root node labeled null For each transaction Sort items according to
   frequency order Insert items into the FP tree updating counts if the path exists Maintain a header table to
   link nodes of the same item Step 3 Mine the FP Tree Start from each item in the header table Construct its
   conditional pattern base sub database of paths leading to the item Build conditional FP tree for each item
   Recursively find frequent patterns 5 Example Transaction Database TID Items 1 A B D E 2 B C E 3 A B D E 4 A B
   C E 5 A B C D E Minimum Support 3 Step 1 Count frequency A 4 B 5 C 3 D 3 E 5 Step 2 Build FP Tree root items
   in descending order B E A D C Step 3 Mine FP Tree to get frequent itemsets B E A D C B E B A B D E A B E A
   etc 6 Summary FP Growth is faster and memory
   + 2026 [2457–2628]:
      their frequency Build the FP tree by inserting the transactions according to this frequency order Create a
      header table that connects nodes representing the same item Mine the FP tree to discover frequent itemsets
      Construct conditional pattern bases and conditional FP trees as needed Continue recursively until all
      frequent patterns are discovered Simple Example Consider the following transactions Transaction Items T1
      Bread Milk T2 Bread Coffee T3 Bread Milk Coffee T4 Milk Coffee T5 Bread Milk Assume The algorithm first
      counts the items Bread 4 Milk 4 Coffee 3 All three items satisfy the minimum support The frequent items
      are then ordered according to their frequency and the transactions are inserted into an FP tree Instead of
      generating as explicit candidate sets like Apriori FP Growth stores the transaction information in the
      tree and mines the tree to discover the frequent patterns Why is FP Growth Useful The main advantages are
      It does not explicitly generate candidate itemsets It uses a compact FP tree to represent transaction data
      It can be more
25. − OLD [2790–2883]:
   avoids candidate generation and uses a compact FP tree structure Frequently used in market basket analysis
   web usage mining and other pattern mining tasks Enumeration Tree Algorithms 1 Introduction Enumeration Tree
   Algorithms are a class of algorithms used in frequent itemset mining and combinatorial optimization They
   systematically explore all possible combinations of items or decisions in a tree like structure called an
   enumeration tree Goal Efficiently enumerate candidate solutions e g frequent itemsets and prune the search
   space using specific criteria to avoid unnecessary exploration 2 Key Concepts Enumeration Tree A conceptual
   tree where
   + 2026 [2636–2769]:
      reduces the problem of generating a very large number of candidate itemsets Apriori vs FP Growth Feature
      Apriori FP Growth Candidate generation Yes No explicit candidate generation Main structure Candidate
      itemsets FP tree Database scanning Multiple scans Typically two main scans to construct the tree followed
      by tree mining Main strategy Generate and prune Compress and grow patterns Large datasets Can become
      expensive Often more efficient In simple terms Apriori generates candidate itemsets and then tests them
      whereas FP Growth builds an FP tree and mines the tree to find frequent itemsets without explicitly
      generating candidates Enumeration Tree Algorithms Enumeration Tree Algorithms An Enumeration Tree is a
      tree based approach for systematically exploring possible combinations of items to find frequent itemsets
      The basic idea is to represent the possible item combinations as a tree
26. − OLD [2889–2903]:
   solution e g a set of items The root is the empty set Branches represent
   + 2026 [2775–2837]:
      itemset and adding an item creates a larger itemset Basic Structure Suppose we have three items The
      enumeration tree can be represented conceptually as A B C A B A C B C A B C The root represents the empty
      itemset The first level represents 1 itemsets The second level represents 2 itemsets The next level
      represents larger itemsets Each branch represents
27. − OLD [2910–2917]:
   partial solution Leaves represent complete candidate solutions Search
   + 2026 [2844–2969]:
      itemset How It Works The general process is Start with an empty itemset Add an item to create a candidate
      itemset Calculate its support Check whether it satisfies the minimum support threshold If the itemset is
      promising continue extending it If it cannot lead to a frequent itemset prune the branch Continue until
      all relevant branches have been explored Pruning Pruning is important because examining every possible
      combination can be expensive For example if then based on the Apriori property any larger itemset
      containing A B cannot be frequent Therefore we can stop exploring that branch A A B Infrequent X Do not
      explore A B C A B D This reduces the search space Search Strategies An enumeration tree can be explored
      using different traversal
28. − OLD [2923–2933]:
   Explore one branch fully before backtracking Breadth First Search BFS Explore
   + 2026 [2975–2992]:
      explores one branch as deeply as possible before returning and exploring another branch Breadth First
      Search BFS explores
29. − OLD [2941–3206]:
   deeper Pruning Techniques Avoid exploring branches that cannot lead to valid solutions Minimum Support
   Pruning If a partial itemset is infrequent its supersets are also infrequent Apriori principle Constraint
   Based Pruning Apply domain specific constraints to prune candidates early 3 How Enumeration Tree Algorithms
   Work Step 1 Construct Enumeration Tree Start with the empty set at the root For each level add an item not
   yet included in the current partial set Continue until all items are considered Step 2 Explore the Tree
   Traverse the tree using DFS or BFS At each node compute relevant metrics e g support count Step 3 Apply
   Pruning If the current node cannot lead to a frequent itemset cut off its subtree This significantly reduces
   the number of candidates explored Step 4 Collect Frequent Itemsets All leaf nodes that satisfy minimum
   support are output as frequent itemsets 4 Advantages Systematic Exploration Guarantees all candidate
   solutions are considered Efficient Pruning Reduces the search space significantly Flexible Can be combined
   with constraints or used in different domains e g association rules combinatorial optimization 5 Example
   Items A B C Minimum Support 2 Enumeration Tree Structure A B C A B A C Traversal Start at root Add A A check
   support Add B A B check support If support min support prune this branch Result Frequent itemsets are A B A B
   etc depending on transaction data 6 Summary Enumeration Tree Algorithms systematically generate candidate
   solutions They use tree structures to represent partial solutions Pruning reduces computation by avoiding
   exploration of invalid branches Widely used in frequent pattern mining and combinatorial problems
   + 2026 [3000–3117]:
      to the next level Advantages Provides a systematic way to explore possible itemsets Can use pruning to
      reduce unnecessary exploration Can be adapted to different constraints and mining problems Helps visualize
      the search space of frequent itemset generation Limitation Without effective pruning the enumeration tree
      can become extremely large because the number of possible itemsets grows exponentially with the number of
      items Simple Definition Enumeration tree algorithms systematically explore possible item combinations
      using a tree structure and use pruning techniques to avoid exploring combinations that cannot produce
      useful or frequent patterns Important distinction An enumeration tree is better understood as a search
      space representation and exploration approach rather than a single specific algorithm like Apriori or FP
      Growth
30. − OLD [3213–3214]:
   1 Introduction
   + 2026 [3124–3129]:
      Recursive Suffix Based Pattern Growth Methods
31. − OLD [3224–3560]:
   in frequent itemset mining particularly in sequential pattern mining These methods focus on growing patterns
   by appending items to the suffix of an existing pattern and using recursion to explore all possible
   extensions efficiently Goal Efficiently find all frequent sequential patterns without generating a large
   number of candidate sequences improving on algorithms like Apriori 2 Key Concepts Suffix Pattern In a
   sequence the suffix is the part of the sequence that comes after a given prefix Example For sequence A B C
   the suffix after prefix A is B C Pattern Growth Start from a small pattern usually length 1 Recursively
   extend it by adding items from its suffix that appear frequently in the database Avoids generating all
   possible candidate sequences like Apriori Recursion At each step Identify frequent items in the current
   suffix database Extend the pattern with these items Recursively apply the method to new patterns until no
   frequent extensions exist 3 How It Works Step 1 Identify Frequent Items Scan the database to find items with
   support minimum support Treat each frequent item as a base pattern Step 2 Construct Projected Database For
   each frequent pattern P build a projected database containing only the suffixes of sequences in which P
   appears Step 3 Recursively Grow Patterns In the projected database Find items frequent in suffixes Append
   each frequent item to the current pattern Recursively repeat for the new pattern using its projected database
   Step 4 Termination Stop recursion when no further items in the suffix are frequent 4 Example Sequence
   Database Sequence ID Sequence 1 A B C 2 A C 3 B C 4 A B Minimum Support 2 Step 1 Frequent 1 item sequences A
   3 B 3 C 3 Step 2 Projected Database for A Suffixes after A B C C B Step 3 Recursively Extend A Frequent in
   suffixes B 2 C 2 Generate patterns A B A C Recursively grow A B suffix C A B C support 2 Resulting frequent
   sequences A B C A B A C
   + 2026 [3139–3349]:
      to discover frequent sequential patterns by extending an existing pattern step by step using items that
      frequently occur in its suffix The main idea is Start with a short pattern examine the sequences that
      follow it and recursively extend the pattern using frequent items from those suffixes This approach is
      commonly associated with sequential pattern mining rather than traditional transaction based association
      rule mining Simple Example Consider the following sequence database Sequence Events S1 A B C S2 A C S3 B C
      S4 A B Suppose the minimum support is 2 sequences First identify frequent single items A 3 sequences B 3
      sequences C 3 sequences Therefore are frequent patterns Growing a Pattern Start with Look at the items
      occurring after A S1 B C S2 C S4 B Therefore B occurs after A in 2 sequences C occurs after A in 2
      sequences Both satisfy the minimum support So we can extend and The process can continue recursively For
      example can be extended with C if C occurs after the pattern in enough sequences Projected Database A key
      concept is the projected database For a particular pattern we create a smaller database containing the
      relevant suffixes of sequences where that pattern occurs For example for the suffixes are S1
32. − OLD [3566–3625]:
   B already counted 5 Advantages Efficient No candidate generation for all possible sequences Compact
   Representation Uses projected databases instead of full candidate sets Recursive Structure Naturally explores
   all frequent patterns 6 Summary Recursive suffix based methods grow patterns by appending frequent items from
   suffixes They recursively explore the projected database for each pattern Commonly used in algorithms like
   PrefixSpan for
   + 2026 [3355–3551]:
      S2 A C C S4 A B B This projected database is then used to find frequent extensions of A General Process
      The method can be summarized as 1 Find frequent items 2 Select a frequent pattern 3 Construct its
      projected database 4 Find frequent items in the projected database 5 Extend the current pattern 6
      Recursively repeat the process 7 Stop when no frequent extension remains Advantages Avoids generating all
      possible sequential candidates Reduces the search space by using projected databases Can efficiently
      discover sequential patterns Uses recursion to grow patterns gradually Example of Its Application Consider
      an online shopping sequence If this sequence occurs frequently among customers sequential pattern mining
      can discover patterns such as or This is different from ordinary association mining because the order of
      events is considered Association vs Sequential Pattern Mining Association mining Focuses mainly on co
      occurrence Sequential pattern mining Focuses on the order in which items or events occur In simple terms
      Recursive suffix based pattern growth finds frequent sequences by repeatedly extending a pattern with
      frequent items found in the suffixes of sequences where the pattern occurs A well known example of this
      approach is PrefixSpan Prefix projected

## SVM/evaluation diagnostic comparison

**المصادر القديمة:** DM_Classification_SVM_Evaluation_Metrics (archive).docx.  **مصادر 2026:** Week6_Classification.docx, Week7_Classification_Techniques.pdf.

**الكلمات المرمّزة:** القديم 2,762؛ الحالي 6,483؛ المتطابق بالترتيب 145. The current set splits foundations/evaluation and methods across Weeks 6–7; the method coverage changed.

1. − OLD [1–532]:
   Support Vector Machine SVM Support Vector Machine SVM is a supervised learning algorithm used for
   classification and regression It tries to Find the best possible boundary decision line or hyperplane that
   separates data points of different classes Example Let’s say we want to classify patients as 0 Non diabetic 1
   Diabetic We have two features Glucose level BMI If we plot them X diabetic BMI O O X Glucose Level SVM finds
   the line that separates O and X with the widest possible margin 2 Step by Step How SVM Works Step 1 Represent
   Data Points Each data point feature vector Each has a label Step 2 Find a Separating Hyperplane A hyperplane
   is just a fancy word for a line in 2D plane in 3D or higher dimensional surface Equation of the hyperplane
   where weight vector direction of the line bias offset from origin This hyperplane divides the space into two
   sides Class 1 Class 1 Step 3 Maximize the Margin SVM doesn’t just find any line that separates the classes it
   finds the one with the largest margin distance between the nearest points from each class The nearest points
   are called Support Vectors So SVM solves this optimization problem subject to This ensures All points are
   correctly classified The margin is as wide as possible Step 4 Find the Optimal Line SVM uses optimization
   techniques like Lagrange multipliers to find The weight vector The bias These define the optimal hyperplane
   Step 5 Use Kernels for Nonlinear Data What if your data can’t be separated by a straight line Example X X X X
   O X X X X No straight line can separate O’s and X’s SVM uses the Kernel Trick It maps the data into a higher
   dimension where it becomes separable Example kernels Linear for simple separable data Polynomial adds curve
   RBF Radial Basis Function handles complex shapes Step 6 Classify New Data Once the model is trained for a new
   data point If Class 1 If Class 1 3 Visual Intuition Before Training O O O X X X O O X X After SVM finds
   hyperplane Margin Boundary Support Vectors O O X X O X Maximum Margin The green line decision boundary The
   parallel dashed lines margin boundaries The points touching those lines support vectors they define the
   boundary 4 Key Concepts in SVM Term Meaning Support Vectors Data points closest to the decision boundary
   Hyperplane Line plane dividing classes Margin Distance between support vectors and boundary Kernel Trick Maps
   data to higher dimensions for non linear separation C Regularization Parameter Controls trade off between
   margin size and classification errors Types of Support Vector Machine Based on the nature of the decision
   boundary Support Vector Machines SVM can be divided into two main parts Linear SVM Linear SVMs use a linear
   decision boundary to separate the data points of different classes When the data can be precisely linearly
   separated linear SVMs are very suitable This means that a single straight line in 2D or a hyperplane in
   higher dimensions can entirely divide the data points into their respective classes A hyperplane that
   maximizes the margin between the classes is the decision boundary Non Linear SVM
   + 2026 [1–278]:
      Classification in Data Mining 1 Introduction to Classification 1 1 Definition of Classification
      Classification is one of the most important techniques in Data Mining and Machine Learning It is used to
      assign a data record to one of a set of predefined classes Simple Definition Classification is the process
      of learning from previously labeled data and using the learned knowledge to assign a class to new data For
      example a hospital may want to determine whether a patient has a particular disease The possible classes
      could be Disease No Disease The classification model learns from previous patients and then predicts the
      class of a new patient 1 2 Why Classification Is Important Classification is important because many real
      world problems require us to make decisions based on available data For example Healthcare Predict whether
      a patient has a disease Banking Predict whether a customer is likely to default on a loan Education
      Predict whether a student will pass or fail Cybersecurity Determine whether network traffic is normal or
      malicious Email Determine whether an email is spam or not spam Business Predict whether a customer will
      leave a company Therefore classification is widely used for prediction and decision making 1 3
      Classification as Supervised Learning Classification is a type of supervised learning The term supervised
      means that the training data contains the correct answers For example consider a dataset containing
      patient information Age Glucose BMI Diabetes 25 110 23 5 No 45 180 31 2 Yes 52 160 29 8 Yes 30 95 22 1 No
      The first three columns describe the patients The last column contains the known class The algorithm
      studies these examples and learns patterns that
2. − OLD [538–2625]:
   data when it cannot be separated into two classes by a straight line in the case of 2D By using kernel
   functions nonlinear SVMs can handle nonlinearly separable data The original input data is transformed by
   these kernel functions into a higher dimensional feature space where the data points can be linearly
   separated A linear SVM is used to locate a nonlinear decision boundary in this modified space Advantages of
   Support Vector Machine SVM High Dimensional Performance SVM excels in high dimensional spaces making it
   suitable for image classification and gene expression analysis Nonlinear Capability Utilizing kernel
   functions like RBF and polynomial SVM effectively handles nonlinear relationships Outlier Resilience The soft
   margin feature allows SVM to ignore outliers enhancing robustness in spam detection and anomaly detection
   Binary and Multiclass Support SVM is effective for both binary classification and multiclass classification
   suitable for applications in text classification Memory Efficiency It focuses on support vectors making it
   memory efficient compared to other algorithms Disadvantages of Support Vector Machine SVM Slow Training SVM
   can be slow for large datasets affecting performance in SVM in data mining tasks Parameter Tuning Difficulty
   Selecting the right kernel and adjusting parameters like C requires careful tuning impacting SVM algorithms
   Noise Sensitivity SVM struggles with noisy datasets and overlapping classes limiting effectiveness in real
   world scenarios Limited Interpretability The complexity of the hyperplane in higher dimensions makes SVM less
   interpretable than other models Feature Scaling Sensitivity Proper feature scaling is essential otherwise SVM
   models may perform poorly What Are Neural Networks A Neural Network NN is a machine learning model inspired
   by how the human brain works It’s made up of layers of interconnected nodes neurons that learn to recognize
   patterns in data They’re especially powerful for Image recognition Speech recognition Natural language
   processing Predictive analytics Basic Structure of a Neural Network A typical feedforward neural network has
   3 main types of layers Layer Type Description Example Input Layer Takes the raw data Features e g pixel
   values numeric data Hidden Layers Process data and learn features Dense fully connected layers Output Layer
   Produces predictions Binary 0 1 or multi class probabilities How Neural Networks Learn Training a neural
   network involves three key steps Forward Propagation Input data flows through the layers The network produces
   an output prediction Loss Calculation Compare the prediction with the actual result using a loss function
   like cross entropy or MSE Backward Propagation Backprop Adjusts the weights to reduce the error using an
   optimizer like Adam or SGD This process repeats for many epochs until the model learns the pattern
   Mathematical Representation For a simple neuron Where input weights bias activation function e g ReLU Sigmoid
   output Activation Functions Activation functions help the network learn complex relationships Function
   Formula Typical Use Sigmoid Binary classification ReLU Most hidden layers Softmax Multi class classification
   Types of Neural Networks Type Description Example Use MLP Multilayer Perceptron Basic feedforward NN for
   structured tabular data Credit scoring health prediction CNN Convolutional Neural Network Learns from image
   data Object detection medical imaging RNN Recurrent Neural Network Works with sequence data Time series
   speech text LSTM GRU Advanced RNNs that remember longer dependencies Sentiment analysis forecasting
   Autoencoder Learns to compress and reconstruct data Dimensionality reduction anomaly detection GAN Generative
   Adversarial Network Two NNs compete to create realistic data Image generation data synthesis Transformer
   Handles long range dependencies ChatGPT BERT translation models Key Advantages Learns complex patterns
   automatically Works with many data types images text numbers Scales to large datasets Disadvantages Requires
   a lot of data and computation Hard to interpret black box Needs careful tuning learning rate architecture etc
   How Neural Networks Work Step by Step A neural network learns to make predictions by repeatedly adjusting its
   internal parameters called weights based on data and errors Let’s walk through the process Step 1 Input Layer
   Feed the Data In Each input neuron receives one feature a number from your data Example for diabetes
   prediction Feature Example Value Age 45 Glucose 160 BMI 32 Blood Pressure 85 These numbers go into the input
   layer of the neural network Each neuron in the input layer passes the value to the next layer Step 2 Hidden
   Layers Learn Patterns Each hidden neuron does a small computation Where input values from the previous layer
   weights what the network learns bias a small adjustment term activation function e g ReLU sigmoid output
   activation value These small computations let the network learn relationships like High glucose high BMI
   likely diabetic The deeper the network more hidden layers the more complex patterns it can learn Step 3
   Output Layer Make a Prediction The final layer combines all learned patterns to output a result Example
   Binary classification 0 no disease 1 disease Multi class classification e g cat dog horse If it’s binary we
   often use a sigmoid activation Which gives a probability between 0 and 1 Step 4 Compare Prediction to Reality
   Loss The network compares its prediction to the true label using a loss function For example true label
   predicted probability The goal is to make this loss as small as possible Step 5 Backpropagation Learn from
   Mistakes Now comes the magic The network uses backpropagation reverse computation to Measure how much each
   weight contributed to the error Adjust the weights in the direction that reduces the error It uses an
   optimizer like Adam or SGD to do this efficiently Each cycle of forward backward adjustment 1 epoch Step 6
   Repeat Until Accuracy Improves The process repeats for many epochs Forward pass prediction Compute loss
   Backpropagate error Update weights Over time the network’s predictions get closer to the truth That’s how it
   learns Analogy Learning Like a Human Think of it like this Human Brain Neural Network Neurons Artificial
   neurons Synapses Weights Learning from experience Adjusting weights via backprop Remembering patterns Storing
   knowledge in weights When you see multiple examples your brain starts recognizing patterns Neural networks do
   exactly that but with math Visualization Example Input Layer Hidden Layer 1 Hidden Layer 2 Output Features
   Extract patterns Combine features Predict class Each layer transforms the data slightly until the output
   layer produces the correct label In Simple Terms Step Process Example 1 Input Feed numeric image data 2
   Forward pass Compute weighted sums 3 Activation Add non linearity ReLU Sigmoid 4 Output Get prediction 5 Loss
   Measure error 6 Backpropagation Adjust weights to reduce error 7 Repeat Keep training until accurate End Goal
   After enough training The model learns weights that map inputs correct outputs You can then feed new data and
   it will predict correctly even for unseen examples What is Classifier Performance Classifier performance is a
   crucial aspect of machine learning that determines the accuracy and effectiveness of a classification model
   It refers to the ability of a classifier to correctly classify instances from a given dataset In simpler
   terms classifier performance is a measure of how well a machine learning model is able to identify and
   categorize different objects or data points Fundamentally classifier performance is evaluated using various
   metrics such as accuracy precision recall and F1 score These metrics provide a quantitative measure of the
   performance of a classifier allowing data scientists and engineers to determine the effectiveness of their
   models However comparing classifiers can be challenging due to differences in the datasets used the
   complexity of the models and the nature of the classification problem Despite the challenges improving
   classifier performance is crucial for many real world applications including image recognition speech
   recognition and natural language processing This article will delve deeper into the fundamentals of
   classifier performance the metrics used for performance evaluation challenges in performance evaluation and
   strategies for improving classifier performance Fundamentals of Classifier Performance In machine learning
   classification is the process of predicting the class or category of a given input data point based on its
   features A classifier is a model that is trained on a dataset of labeled examples to make these predictions
   The accuracy of a classifier is determined by how well it can correctly classify new unseen examples Why do
   we perform classifier evaluation Classifier performance evaluation is a critical step in machine learning
   model development It helps to assess the accuracy and reliability of a classifier and to identify areas for
   improvement By evaluating the performance of a classifier on a test set of data we can determine how well it
   generalizes to new unseen examples This is important because a classifier that performs well on the training
   data but poorly on the test data is overfit and will not generalize well to new data To evaluate classifier
   performance we use a variety of metrics such as accuracy precision recall F1 score and ROC curve These
   metrics provide different perspectives on the performance of a classifier and can be used to compare
   different models or to tune the parameters of a single model It is important to choose the appropriate metric
   s based on the problem at hand and to interpret the results in the context of the specific application When
   evaluating a classifier we want to estimate how well it will perform on unseen data However if we use the
   same data for both training and testing we’ll get unrealistically high accuracy So we need methods that
   fairly assess model performance The three most common ones are Holdout Method The simplest evaluation
   approach you split the dataset into two parts 60 Train 20 Validation 20 Test 70 Train 15 Validation 15 Test
   Example If you have 1 000 samples 700 Training 150 Validation 150 Testing Workflow Example Let’s say you’re
   building an image classifier Train on the training set Validate using the validation set to tune
   hyperparameters Adjust model parameters like learning rate batch size number of layers etc until you get the
   best validation accuracy Finally test on the test set only once Why We Need a Validation Set Without it You
   might tune your model on the test set which causes data leakage and overestimates performance The model might
   overfit the training data and perform poorly on new data With a validation set You can fine tune safely The
   test set remains completely unseen gives a true measure of generalization Advantages Simple and fast Works
   well with large datasets Disadvantages The result depends heavily on how the data is split If the split is
   not representative results may be misleading For example if most positive cases fall into the training set
   and few in testing accuracy might be inaccurate Cross Validation A more reliable way to evaluate a model
   especially when data is limited The dataset is divided into k equal parts folds Then the model is trained and
   tested k times each time using a different fold as the test set and the remaining folds as training data
   Example 5 fold cross validation Train on 4 folds test on 1 repeat 5 times Final performance average of all 5
   runs How It Works Split data into k folds e g 5 or 10 For each fold Train on k 1 folds Test on the remaining
   fold Average the metrics accuracy F1 etc over all folds Advantages Every instance is used for both training
   and testing Reduces bias due to random data splitting Provides a more stable and realistic performance
   estimate Disadvantages Computationally more expensive model trained k times Still might not handle extreme
   data imbalance perfectly Bootstrap Method A sampling based evaluation method that uses resampling with
   replacement to create multiple training test datasets How It Works Randomly sample the dataset with
   replacement to create a new training set This means some samples may appear multiple times and some may not
   appear at all Use the samples not selected as the test set Train and evaluate the model on many e g 1000
   bootstrap samples Average the results Advantages Works well when the dataset is small Gives a good estimate
   of the model’s variance and bias Disadvantages May include duplicate samples in the training data
   Computationally intensive Summary Table Method Description Pros Cons Best Use Holdout Split once into train
   test Simple fast High variance data split bias Large datasets Cross Validation k fold rotation of train test
   Reliable balanced Slower more computation Small medium datasets Bootstrap Sampling with replacement Good for
   small data variance estimate Complex duplicates data Very small datasets or statistical analysis Common
   Evaluation Metrics 1 Accuracy Measures overall correctness TP True Positives TN True Negatives FP False
   Positives FN False Negatives Simple to understand but misleading if classes are imbalanced 2 Confusion Matrix
   Shows exactly where the model is right or wrong
   + 2026 [284–1265]:
      new patients Basic Idea Labeled Data Classification Algorithm Classification Model New Data Predicted
      Class 1 4 Applications of Classification Classification is used in many areas Medical Applications Disease
      diagnosis Cancer classification Patient risk classification Financial Applications Fraud detection Credit
      risk classification Loan approval Educational Applications Student performance prediction Student dropout
      prediction Pass and fail prediction Cybersecurity Applications Malware classification Intrusion detection
      Phishing detection Business Applications Customer churn prediction Customer response prediction Product
      classification Text Mining Applications Spam detection Sentiment classification Document classification
      Image Applications Object classification Face recognition Medical image classification 2 Basic Concepts of
      Classification Before studying classification algorithms students need to understand several important
      terms 2 1 Dataset A dataset is a collection of data records For example a medical dataset may contain
      information about thousands of patients A student dataset may contain information about Student age
      Attendance Grades Study hours Final result 2 2 Instance An instance is one individual record in a dataset
      For example One patient is one instance One student is one instance One email is one instance In a table
      an instance is usually represented by one row 2 3 Feature A feature is an attribute that describes an
      instance For example patient features may include Age Weight Blood pressure Glucose BMI Features are also
      called Attributes Variables Predictors Features are used by the classification model to make predictions 2
      4 Class Label The class label is the category that we want to predict Examples Diabetes Yes No Cancer
      Benign Malignant Student Performance Pass Fail Email Spam Not Spam The class label is also commonly called
      the target variable 2 5 Training Data Training data is the data used to teach the classification algorithm
      It contains Features Known class labels The algorithm examines the training data and learns patterns 2 6
      Validation Data Validation data is used during model development It can help us Select between different
      models Tune model settings Detect overfitting Choose the best model Validation data is particularly useful
      when developing more complex models 2 7 Test Data Test data is used to evaluate the final classification
      model The model should not use the test data during training The purpose is to determine how well the
      model performs on unseen data 3 How Classification Works Classification normally involves several stages 3
      1 Model Training First we provide the algorithm with training data For example Study Hours Attendance
      Previous Grade Result 2 60 50 Fail 4 75 65 Pass 6 90 80 Pass 1 50 40 Fail 5 85 75 Pass The algorithm
      examines the relationship between the features and the class It tries to learn patterns that distinguish
      one class from another 3 2 Model Testing After training the model is evaluated using data that it has not
      seen during training For example Study Hours Attendance Previous Grade Actual Result 3 70 55 Fail 6 88 82
      Pass The model predicts the results We then compare the predictions with the actual results 3 3
      Classification of New Data Once we are satisfied with the model's performance we can use it to classify
      new records For example New student Study hours 5 Attendance 88 percent Previous grade 78 The model may
      predict Pass The model made this prediction based on patterns learned from previous students 3 4 Example
      of a Classification Problem Consider a hospital that wants to classify patients into High Risk Low Risk
      The hospital has historical patient data Features may include Age Blood pressure Cholesterol Weight
      Previous medical history The model learns from previous patients When a new patient arrives the model
      predicts High Risk or Low Risk 4 Types of Classification There are several types of classification
      problems 4 1 Binary Classification Binary classification contains two classes Examples Email Spam Not Spam
      Medical Diagnosis Disease No Disease Education Pass Fail Banking Fraud Not Fraud Binary classification is
      one of the most common types of classification 4 2 Multiclass Classification Multiclass classification
      contains more than two classes For example an image classification system may classify images into Cat Dog
      Horse Bird Another example is disease classification Diabetes Heart Disease Kidney Disease Healthy The
      model normally assigns one class to each instance 4 3 Multilabel Classification In multilabel
      classification one instance can belong to more than one class at the same time For example a research
      paper could be classified as Artificial Intelligence Machine Learning Data Mining The paper can belong to
      all three categories Difference Multiclass One instance One class Multilabel One instance Multiple classes
      4 4 Classification and Regression Classification and regression are both supervised learning techniques
      but they predict different types of outputs Classification Predicts a category Example Patient Disease or
      No Disease Regression Predicts a numerical value Example Patient Expected blood glucose level Therefore
      Classification predicts categories while regression predicts numerical values 4 5 Classification and
      Clustering Classification and clustering are often confused They are different techniques Classification
      Clustering Supervised learning Unsupervised learning Uses labeled data Uses unlabeled data Classes are
      already known Groups are discovered Used for prediction Used to discover patterns Example If we know that
      emails are Spam Not Spam and we train a model to classify new emails this is classification If we have
      thousands of emails without labels and want to discover groups of similar emails this is clustering 5
      Classification Algorithms There are many classification algorithms The most important algorithms include
      Decision Tree Naive Bayes K Nearest Neighbors Support Vector Machine Logistic Regression Random Forest
      Neural Networks 6 Classification Model Evaluation After building a classification model we need to
      determine how well it performs Model evaluation is important because a model that performs well on
      training data may not necessarily perform well on new data Important evaluation measures include Confusion
      Matrix Accuracy Precision Recall Specificity F1 score ROC Curve AUC 6 1 Confusion Matrix A confusion
      matrix shows the correct and incorrect predictions made by a classification model For binary
      classification
3. − OLD [2634–2673]:
   TP False Negative FN Actual Negative False Positive FP True Negative TN Example visualization from sklearn
   metrics import confusion matrix ConfusionMatrixDisplay cm confusion matrix y test y pred
   ConfusionMatrixDisplay cm plot 3 Precision How many predicted positives are actually correct
   + 2026 [1274–1465]:
      False Negative Actual Negative False Positive True Negative 6 2 True Positive The actual class is positive
      The model also predicts positive Example A patient has cancer The model predicts cancer This is a True
      Positive 6 3 True Negative The actual class is negative The model also predicts negative Example A patient
      does not have cancer The model predicts no cancer This is a True Negative 6 4 False Positive The actual
      class is negative The model predicts positive Example A patient does not have cancer The model predicts
      cancer This is a False Positive This can be considered a false alarm 6 5 False Negative The actual class
      is positive The model predicts negative Example A patient has cancer The model predicts no cancer This is
      a False Negative In some medical applications false negatives can be particularly serious 6 6 Accuracy
      Accuracy measures the percentage of all predictions that are correct For example Suppose there are 100
      patients The model correctly classifies 95 patients The accuracy is 95 percent Accuracy is easy to
      understand but it should not always be used alone 6 7 Precision Precision answers the question
4. − OLD [2683–2690]:
   right 4 Recall Sensitivity How many actual positives
   + 2026 [1475–1524]:
      correct Formulas For example The model predicts that 100 patients have a disease Only 90 actually have the
      disease The precision is 90 percent Precision is important when false positive predictions are costly 6 8
      Recall Recall answers the question Of all the cases that are actually positive how many
5. − OLD [2696–2700]:
   Of all the actual positives
   + 2026 [1530–1580]:
      For example There are 100 patients who actually have a disease The model correctly identifies 95 of them
      The recall is 95 percent Recall is especially important when missing a positive case can have serious
      consequences 6 9 Specificity Specificity answers the question Of all the cases that are actually negative
6. − OLD [2706–2762]:
   find 5 F1 Score Balances precision and recall useful when you want both to be high 6 ROC Curve and AUC ROC
   Receiver Operating Characteristic curve plots True Positive Rate Recall False Positive Rate 1 Specificity AUC
   Area Under the Curve measures how well the model separates classes AUC 1 perfect classifier AUC 0 5 random
   guessing
   + 2026 [1586–6483]:
      correctly identify For example There are 100 healthy patients The model correctly identifies 90 of them as
      healthy The specificity is 90 percent 6 10 F1 Score F1 score combines precision and recall into one
      measure It is particularly useful when The dataset is imbalanced Both false positives and false negatives
      are important A high F1 score means that the model has a good balance between precision and recall 6 11
      ROC Curve The ROC curve is used mainly for binary classification It evaluates the model at different
      decision thresholds It considers two important aspects How well the model identifies positive cases How
      often the model incorrectly identifies negative cases as positive A model with better separation between
      the classes generally has a better ROC curve 6 12 AUC AUC means Area Under the ROC Curve It provides a
      single value that summarizes the model's ability to distinguish between classes Generally AUC General
      Interpretation 0 50 Random performance 0 60 0 70 Poor 0 70 0 80 Acceptable 0 80 0 90 Good 0 90 1 00
      Excellent These values should be considered general guidelines rather than strict rules 7 Problems in
      Classification Classification models can face several problems The most important are Class imbalance
      Overfitting Underfitting Irrelevant features Missing data Noisy data 7 1 Class Imbalance Class imbalance
      occurs when one class contains significantly more records than another For example Class Number Healthy 9
      000 Disease 1 000 The dataset is imbalanced Suppose a model predicts every patient as healthy The model
      would achieve 90 percent accuracy However it would fail to identify any patient with the disease Therefore
      High accuracy does not always mean that a classification model is good 7 2 Overfitting Overfitting occurs
      when the model learns the training data too closely For example Training accuracy 99 percent Testing
      accuracy 70 percent The large difference suggests that the model may have learned the training data rather
      than learning general patterns Causes Model is too complex Dataset is too small Too many features Noisy
      data Insufficient regularization 7 3 Underfitting Underfitting occurs when the model is too simple to
      learn the important patterns in the data For example Training accuracy 65 percent Testing accuracy 63
      percent The model performs poorly on both training and testing data Possible solutions include Using a
      more appropriate algorithm Adding useful features Reducing excessive regularization Improving the quality
      of the data 7 4 Irrelevant Features Not every feature in a dataset is useful For example suppose we want
      to predict whether a patient has diabetes Useful features may include Age Glucose BMI Blood pressure An
      unrelated feature may add noise without helping the prediction Too many irrelevant features can Increase
      complexity Increase training time Reduce model performance Increase the risk of overfitting 7 5 Missing
      Data Real world datasets often contain missing values For example Age Glucose BMI 45 180 31 52 Missing 29
      30 95 22 Missing data must be handled appropriately before training many classification models Possible
      approaches include Removing records Replacing missing values Using statistical imputation Using model
      based imputation The appropriate approach depends on the dataset and the reason for the missing values 7 6
      Noisy Data Noise refers to incorrect inconsistent or unnecessary information in the dataset Examples
      include Incorrect measurements Typographical errors Incorrect labels Extreme values caused by measurement
      errors Data cleaning is an important step before classification 8 Improving Classification Performance
      Several techniques can improve classification performance 8 1 Data Preprocessing Data preprocessing
      prepares the dataset before model training It may include Handling missing values Removing duplicates
      Correcting errors Encoding categorical data Scaling numerical features Good preprocessing can
      significantly affect model performance 8 2 Feature Selection Feature selection means choosing the most
      useful features Suppose a dataset contains 100 features Only 20 may be strongly related to the target
      class Using the most useful features can Reduce complexity Reduce training time Reduce overfitting Improve
      interpretability Sometimes improve prediction performance Common techniques include Information Gain Chi
      Square Correlation Mutual Information Recursive Feature Elimination Feature Importance 8 3 Feature Scaling
      Feature scaling ensures that numerical features have comparable scales For example Age may range from 18
      to 80 Income may range from 1 000 to 100 000 The large difference in scale can affect algorithms such as
      KNN SVM Logistic Regression Neural Networks Common scaling methods include Standardization Min Max Scaling
      Robust Scaling 8 4 Handling Class Imbalance Several techniques can be used Oversampling Increase the
      number of minority class examples Undersampling Reduce the number of majority class examples SMOTE SMOTE
      creates synthetic examples for the minority class Class Weights Give greater importance to minority class
      errors Appropriate Evaluation Measures Use Precision Recall F1 score Specificity AUC rather than relying
      only on accuracy 8 5 Cross Validation Cross validation is used to obtain a more reliable estimate of model
      performance In five fold cross validation the dataset is divided into five parts The model is trained and
      evaluated several times Each part is used as the validation set while the remaining parts are used for
      training The results are then averaged Cross validation is especially useful when the available dataset is
      not very large 8 6 Hyperparameter Tuning Classification algorithms contain settings called hyperparameters
      Examples include KNN Number of neighbors Decision Tree Maximum tree depth Random Forest Number of trees
      SVM Kernel and other model settings Hyperparameter tuning attempts to find suitable values for these
      settings Common methods include Grid Search Random Search Bayesian Optimization 8 7 Ensemble Methods An
      ensemble method combines multiple models to produce a stronger prediction Examples include Random Forest
      Gradient Boosting AdaBoost XGBoost The main idea is that combining several models can sometimes produce
      better and more stable results than using one model alone 9 Classification Workflow A complete
      classification project normally follows a sequence of steps Step 1 Data Collection Collect the required
      dataset Step 2 Data Understanding Study Number of records Features Classes Data types Class distribution
      Step 3 Data Cleaning Handle Missing values Duplicate records Incorrect values Noise Step 4 Data
      Preparation Perform appropriate Encoding Scaling Transformation Step 5 Feature Selection Select useful
      features Step 6 Data Splitting Divide the data into appropriate training validation and testing sets Step
      7 Model Training Train one or more classification algorithms Step 8 Model Evaluation Evaluate the models
      using appropriate performance measures Step 9 Model Tuning Improve the selected model by tuning its
      hyperparameters Step 10 Final Prediction Use the final model to classify new unseen data 10 Comparison of
      Classification Algorithms Algorithm Main Strength Main Weakness Decision Tree Easy to understand Can
      overfit Naive Bayes Fast and simple Strong independence assumption KNN Simple and intuitive Can be slow
      with large datasets SVM Good for complex boundaries Can require careful parameter tuning Logistic
      Regression Simple and interpretable Limited for complex relationships Random Forest Robust and accurate
      Less interpretable Neural Network Powerful for complex data Requires careful training There is no single
      classification algorithm that is best for every dataset The best choice depends on Dataset size Number of
      features Data type Class distribution Complexity of the problem Required interpretability Computational
      resources 11 Applications of Classification Classification has many real world applications 11 1
      Healthcare Examples Disease diagnosis Cancer classification Patient risk prediction Medical image
      classification 11 2 Banking and Finance Examples Fraud detection Loan approval Credit risk classification
      Customer risk assessment 11 3 Education Examples Student performance prediction Dropout prediction Pass
      and fail prediction Student risk classification 11 4 Cybersecurity Examples Intrusion detection Malware
      classification Phishing detection Network traffic classification 11 5 Business Examples Customer churn
      prediction Customer response prediction Product classification Customer risk classification 11 6 Text
      Mining Examples Spam detection Sentiment analysis News classification Document classification 11 7 Image
      Classification Examples Face recognition Object classification Medical image classification Animal
      classification 12 Practical Classification Example Breast Cancer Classification Consider a breast cancer
      dataset The dataset contains information about breast tumors Features Examples include Tumor size Cell
      characteristics Texture Shape Other medical measurements Classes The target class may be Benign Malignant
      Practical Process Step 1 Load the dataset Step 2 Examine the features and classes Step 3 Check for missing
      values Step 4 Check whether the classes are balanced Step 5 Prepare the features Step 6 Divide the data
      into training and testing sets Step 7 Train several classification algorithms Logistic Regression Decision
      Tree KNN SVM Random Forest Step 8 Evaluate each model Use Accuracy Precision Recall Specificity F1 score
      AUC Step 9 Compare the results Step 10 Select the most appropriate model The best model should not
      necessarily be the model with the highest accuracy For a medical application recall and specificity may be
      particularly important LECTURE RULE BASED CLASSIFIERS Course Data Mining Topic Classification Techniques
      Level Master's Students 1 Introduction Classification is a supervised learning technique in data mining
      used to assign data objects to predefined classes A model learns from labeled training data and uses that
      knowledge to predict the class of new data A rule based classifier uses a collection of IF THEN rules to
      assign class labels Example IF attendance is high AND the exam mark is at least 50 THEN the student passes
      2 Definition and Structure A rule based classifier represents classification knowledge in the form IF
      condition THEN class Antecedent the IF part containing the conditions that must be satisfied Consequent
      the THEN part containing the predicted class Example IF Age 30 AND Income High THEN Loan Status Approved
      Here Age 30 AND Income High is the antecedent and Loan Status Approved is the consequent 3 Conditions and
      Logical Operators A rule can contain one or more conditions connected by logical operators such as AND and
      OR Example IF Attendance 75 AND Exam Mark 50 THEN Result Pass The AND operator means both conditions must
      be true for the rule to apply An OR operator means at least one of its connected conditions must be true 4
      How Rule Based Classification Works 1 Prepare the dataset by collecting and cleaning the data 2 Generate
      IF THEN rules from the training data 3 Evaluate how accurately the rules classify training examples 4
      Apply the rules to a new data record 5 Assign the predicted class based on the matching rule or rules
      Example dataset Student Attendance Exam mark Result S1 90 80 Pass S2 85 65 Pass S3 60 45 Fail S4 50 35
      Fail S5 80 40 Fail Possible rules Rule 1 IF Exam Mark 50 THEN Result Pass Rule 2 IF Exam Mark 50 THEN
      Result Fail Student S1 has a mark of 80 so Rule 1 predicts Pass Student S3 has a mark of 45 so Rule 2
      predicts Fail 5 Types of Rule Based Classifiers 5 1 Ordered Rules Rules are evaluated in a specific
      sequence The first matching rule determines the predicted class Therefore rule order can affect the result
      when multiple rules match 5 2 Unordered Rules Rules do not necessarily have a fixed priority If multiple
      rules match the classifier may use voting rule quality or another conflict resolution strategy 5 3 Default
      Rule A default rule handles a record when no explicit rule matches Rule 1 IF Exam Mark 50 THEN Result Pass
      Rule 2 IF Exam Mark 40 THEN Result Fail Default Result Fail A mark of 45 matches neither explicit rule so
      the default rule assigns Fail 6 Rule Coverage and Rule Accuracy 6 1 Rule Coverage Coverage is the
      proportion of records that satisfy a rule's conditions Coverage R Number of records satisfying R Total
      number of records Example If 40 of 100 students satisfy a rule coverage 40 100 0 40 or 40 6 2 Rule
      Accuracy Rule accuracy is the proportion of records covered by a rule that belong to the class predicted
      by that rule Accuracy R Correctly classified covered records All records covered by R Example If a rule
      covers 40 students and correctly classifies 36 accuracy 36 40 0 90 or 90 Coverage measures how many
      records a rule applies to Accuracy measures how often the rule predicts the correct class among those
      records 7 Conflict Resolution A conflict occurs when two or more rules match the same record but predict
      different classes Rule 1 IF Attendance 75 THEN Result Pass Rule 2 IF Exam Mark 50 THEN Result Fail A
      student with 80 attendance and a mark of 40 matches both rules which predict different classes Common
      conflict resolution approaches include Rule priority prefer the rule with higher priority Rule ordering
      use the first matching rule Rule quality select the rule with stronger performance on training data Voting
      matching rules vote for a class Default class use a predefined class when needed 8 How Classification
      Rules Are Generated 8 1 Direct Rule Generation Some algorithms learn rules directly from training data by
      identifying conditions that frequently correspond to particular classes 8 2 Extracting Rules from Decision
      Trees A decision tree can be converted into IF THEN rules Each path from the root to a leaf becomes a rule
      IF Exam Mark 50 THEN Result Pass IF Exam Mark 50 THEN Result Fail 8 3 Sequential Covering Sequential
      covering generates rules one at a time 6 Find a rule that correctly classifies a group of training records
      7 Add the rule to the rule set 8 Remove or set aside covered records depending on the algorithm 9 Repeat
      to learn additional rules 10 Stop when a suitable stopping condition is reached RIPPER is an example of a
      rule learning algorithm that uses a sequential covering approach 9 Common Algorithms Algorithm Main idea
      OneR Builds a simple classifier using one attribute RIPPER Learns rules using sequential covering and
      simplifies them CN2 Learns classification rules using heuristic search PART Generates rules from partial
      decision trees 10 Advantages Interpretability rules are usually easy to understand Transparency a
      prediction can be explained by showing the matching rule Flexibility rules can combine multiple attributes
      Knowledge representation rules express knowledge in a human readable form Practical implementation simple
      rules can be implemented with conditional statements 11 Limitations Conflicting rules may predict
      different classes Complex datasets may require a large number of rules Overfitting can occur when rules
      describe training examples too specifically Some records may not match any explicit rule Large rule sets
      can be difficult to maintain Rule pruning rule ordering default classes and validation on unseen data can
      help address these limitations 12 Rule Based Classifiers vs Decision Trees Feature Rule Based Classifier
      Decision Tree Representation IF THEN rules Tree structure Prediction Evaluate applicable rules Follow a
      path from root to leaf Interpretability Often clear for small rule sets Often clear for small trees
      Overlapping conditions Possible One path is followed in a standard tree Generation Learned directly or
      extracted Built by recursively splitting data Complexity May contain overlapping rules May contain many
      branches and leaves A decision tree can be converted into rules but a rule based classifier does not have
      to originate from a decision tree 13 Practical Example Loan Approval Suppose a bank classifies loan
      applications as Approved or Rejected using income and credit history Rule 1 IF Credit History Good AND
      Income High THEN Loan Status Approved Rule 2 IF Credit History Poor THEN Loan Status Rejected Rule 3 IF
      Income Low THEN Loan Status Rejected Default rule Loan Status Rejected An applicant with good credit
      history and high income satisfies Rule 1 and is predicted as Approved An applicant with poor credit
      history matches Rule 2 and is predicted as Rejected In real lending systems rules must be validated and
      comply with applicable regulations 14 Summary A rule based classifier is a supervised classification
      technique that uses IF THEN rules to assign class labels Each rule contains an antecedent conditions and a
      consequent predicted class Key concepts include rule generation and application ordered and unordered
      rules coverage and accuracy conflict resolution default classes and the advantages and limitations of rule
      based classification Rule based classifiers are particularly useful when understanding why a prediction
      was made is as important as obtaining the prediction itself Important distinction During training the
      output labels guide the creation and selection of rules During prediction the output is unknown so the
      classifier applies the learned rules to the input attributes to predict the class NAIVE BAYES ALGORITHM 1
      Introduction Naive Bayes is a supervised machine learning algorithm used for classification It predicts
      the class of a new record by calculating the probability that the record belongs to each possible class It
      is based on Bayes theorem and assumes that input attributes are conditionally independent given the class
      Applications include email spam detection sentiment analysis medical diagnosis document classification and
      weather prediction 2 Bayes Theorem Bayes theorem calculates the probability of a class given observed
      evidence P C X P X C x P C P X Where P C X Posterior probability probability of class C given attributes X
      P X C Likelihood probability of observing X when the class is C P C Prior probability probability of class
      C before considering the attributes P X Evidence overall probability of observing X Observed attributes
      update our estimate of which class is most likely 3 Why Is It Called Naive Bayes It is called naive
      because it assumes input attributes are conditionally independent when the class is known For example a
      student classifier might use attendance study hours and assignment completion to predict Pass or Fail
      Naive Bayes assumes these attributes are conditionally independent given the result Real attributes may be
      related but the algorithm can still perform well 4 How Naive Bayes Works The algorithm generally follows
      these steps 11 Collect labeled training data 12 Calculate the prior probability of each class 13 Calculate
      the likelihood of each attribute value for each class 14 Calculate a score or posterior probability for
      each candidate class 15 Predict the class with the highest score Predicted class argmax over C of P C x P
      X C Under the conditional independence assumption the likelihood is calculated as a product P X C P x1 C x
      P x2 C x x P xn C The evidence P X is the same for each candidate class so it can be omitted when
      comparing class scores 5 Worked Example Weather Prediction Suppose we predict whether people will play
      outside based on Weather and Temperature Weather Temperature Play Sunny Mild Yes Sunny Hot No Rainy Mild
      Yes Rainy Cold No Sunny Mild Yes Rainy Mild No Sunny Mild Yes Rainy Cold No New record Weather Sunny
      Temperature Mild Predict Play Step 1 Calculate prior probabilities There are 8 records 4 have Play Yes and
      4 have Play No P Yes 4 8 0 5 P No 4 8 0 5 Step 2 Calculate likelihoods Among the four Yes records three
      are Sunny and all four have Mild temperature P Sunny Yes 3 4 0 75 P Mild Yes 4 4 1 Among the four No
      records one is Sunny and one has Mild temperature P Sunny No 1 4 0 25 P Mild No 1 4 0 25 Step 3 Calculate
      class scores For Play Yes Score Yes 0 5 x 0 75 x 1 0 375 For Play No Score No 0 5 x 0 25 x 0 25 0 03125
      Step 4 Choose the highest score The Yes score 0 375 is greater than the No score 0 03125 so the prediction
      is Play Yes After normalization the probabilities are approximately 92 3 for Yes and 7 7 for No The
      unnormalized scores are sufficient for comparing classes 6 Zero Probability and Laplace Smoothing If an
      attribute value never occurs in a class its estimated likelihood is zero Multiplying by zero can make the
      entire score for that class zero Laplace smoothing adds a small count to each possible value For a
      categorical attribute P xi C N xi C alpha N C alpha x K N xi C is the number of records in class C with
      value xi N C is the total records in class C K is the number of possible attribute values alpha is the
      smoothing parameter commonly 1 7 Types of Naive Bayes Type Suitable data Example Gaussian Naive Bayes
      Continuous numeric attributes Height weight laboratory measurements Multinomial Naive Bayes Count data
      Word counts in documents Bernoulli Naive Bayes Binary attributes Whether a word occurs or does not occur
      Gaussian Naive Bayes assumes numeric attributes follow a Gaussian distribution within each class
      Multinomial Naive Bayes is often used for word frequency counts Bernoulli Naive Bayes is useful for binary
      features 8 Advantages Simple and computationally efficient Works well for many high dimensional datasets
      Requires relatively little training data for some problems Supports multiple classes Provides class
      probability estimates 9 Limitations The conditional independence assumption may not hold Zero
      probabilities can cause problems without smoothing Probability estimates may be poorly calibrated
      Performance may be weaker when attributes are strongly dependent 10 Naive Bayes vs Rule Based Classifiers
      Feature Naive Bayes Rule Based Classifier Main approach Probability calculations IF THEN rules Training
      Estimates prior and likelihood probabilities Learns or receives classification rules Prediction Chooses
      the most probable class Applies matching rules Assumptions Commonly assumes conditional independence
      Depends on rule learning method Interpretability Uses class probabilities Individual rules are often easy
      to explain 11 Student Exercises 16 A dataset contains 100 records 60 belong to Class A and 40 to Class B
      Calculate both prior probabilities 17 In Class A 30 out of 60 records have Weather Sunny Calculate P Sunny
      A 18 If P A 0 6 P Sunny A 0 5 and P Mild A 0 8 calculate the Naive Bayes score for Class A 19 Explain why
      Naive Bayes is called naive 20 Explain the purpose of Laplace smoothing Exercise Answers 21 P A 60 100 0 6
      P B 40 100 0 4 22 P Sunny A 30 60 0 5 23 Score A 0 6 x 0 5 x 0 8 0 24 24 It assumes attributes are
      conditionally independent given the class 25 It prevents zero likelihood estimates by adding a small count
      to possible attribute values 12 Summary Naive Bayes is a probabilistic classification algorithm based on
      Bayes theorem It uses prior probabilities and likelihoods to estimate the most probable class Essential
      concepts include prior probability likelihood posterior probability conditional independence Laplace
      smoothing and selecting the class with the highest score The key difference from a rule based classifier
      is that Naive Bayes calculates class probabilities whereas a rule based classifier uses IF THEN conditions
      Logistic Regression Algorithm A Lecture for Machine Learning and Data Mining Students Learning Objectives
      Define Logistic Regression and explain its main purpose Understand the sigmoid function and how it
      converts a linear score into a probability Follow the main steps used to train and apply a Logistic
      Regression model Calculate predicted probabilities and convert them into class labels using a decision
      threshold Understand common evaluation metrics advantages and limitations 1 Introduction Logistic
      Regression is a supervised machine learning algorithm used mainly for classification It estimates the
      probability that an observation belongs to a particular class Although its name contains the word
      regression it is commonly used for classification tasks Examples include predicting whether a student will
      pass or fail whether a customer will leave a service whether an email is spam or whether a medical test
      result is positive or negative 2 Types of Logistic Regression Binary Logistic Regression predicts one of
      two classes such as Yes or No Multinomial Logistic Regression predicts one of three or more unordered
      classes Ordinal Logistic Regression models categories that have a meaningful order such as Low Medium and
      High Specific ordinal models use assumptions that differ from ordinary binary Logistic Regression 3 How
      Logistic Regression Works Logistic Regression first calculates a linear score from the input features It
      then applies the sigmoid function to convert that score into a value between 0 and 1 interpreted as a
      probability The linear score is z b b x b x b x where x x x are input features b is the intercept bias b b
      b are learned model coefficients z is the linear score 4 The Sigmoid Function The sigmoid function is P Y
      1 X 1 1 e The sigmoid function maps any real valued score z to a value strictly between 0 and 1 This
      output can be interpreted as the estimated probability of the positive class For example If z 0 then P Y 1
      X 1 1 e 0 5 If z 2 then P Y 1 X 1 1 0 1353 0 8808 If z 2 then P Y 1 X 1 1 7 389 0 1192 5 Decision
      Threshold and Class Prediction For binary classification a threshold converts the estimated probability
      into a class label A common default is 0 5 although the threshold can be adjusted for the task If P Y 1 X
      0 5 predict Class 1 If P Y 1 X 0 5 predict Class 0 Example if the predicted probability is 0 78 and the
      threshold is 0 5 the predicted class is 1 This does not mean the model is 78 accurate it means the model
      estimates a 78 probability for Class 1 6 Worked Numerical Example Suppose we want to predict whether a
      student passes an exam Pass 1 Fail 0 based on the number of hours studied For illustration assume a
      trained Logistic Regression model has the following equation z 4 1 2x where x is the number of hours
      studied The intercept and coefficient are assumed to have been learned during training Example A A student
      studies for 4 hours Step 1 Calculate the linear score z 4 1 2 4 0 8 Step 2 Apply the sigmoid function P
      Pass 1 x 4 1 1 e 1 1 0 4493 0 6900 Step 3 Apply the threshold of 0 5 Because 0 6900 0 5 predict Pass Class
      1 Example B A student studies for 2 hours z 4 1 2 2 1 6 P Pass 1 x 2 1 1 e 0 1680 Because 0 1680 0 5
      predict Fail Class 0 These calculations demonstrate prediction after training In a real application the
      coefficients are estimated from labeled training data 7 Main Training Steps 26 Prepare data Collect
      labeled examples and identify the input features and target class 27 Preprocess features Handle missing
      values and encode categorical inputs when necessary Scaling numeric features can help optimization
      especially when feature magnitudes differ 28 Split the data Separate training data from validation or test
      data to evaluate generalization 29 Initialize the model Set up the Logistic Regression model and its
      training objective 30 Learn coefficients Estimate the intercept and feature coefficients by optimizing the
      logistic loss commonly binary cross entropy often with regularization 31 Estimate probabilities For each
      new record calculate z and apply the sigmoid function 32 Assign a class Compare the probability with a
      chosen decision threshold 33 Evaluate Assess predictions on held out data using appropriate metrics 8 How
      Are the Coefficients Learned The coefficients are not normally chosen by hand The training algorithm
      adjusts them to make the predicted probabilities fit the observed labels For binary classification a
      common objective is binary cross entropy log loss L 1 N y log p 1 y log 1 p Here N is the number of
      training examples y is the actual label 0 or 1 and p is the predicted probability for Class 1 Optimization
      methods such as gradient based methods or solver specific methods minimize this loss Regularization may be
      added to reduce overfitting 9 Interpreting Coefficients A coefficient describes the change in the log odds
      of the positive class associated with a one unit increase in that feature holding the other features
      constant The odds ratio for a one unit increase is exp b For example if b 0 7 then exp 0 7 2 01 Under the
      model a one unit increase in that feature multiplies the odds of Class 1 by about 2 01 holding other
      features constant This is an odds interpretation not a direct doubling of probability 11 Advantages Simple
      to implement and relatively fast to train Produces probabilities that can support threshold based
      decisions Coefficients can be interpreted through log odds and odds ratios Provides a strong baseline for
      many binary classification problems Can use regularization to help control overfitting 12 Limitations The
      basic model assumes a linear relationship between input features and the log odds of the outcome It may
      not capture complex nonlinear patterns unless features are transformed or interactions are added
      Performance can be affected by outliers multicollinearity poor feature design or data quality A
      probability estimate is not automatically well calibrated calibration should be checked when important The
      default 0 5 threshold may not be suitable when false positives and false negatives have different costs 13
      Logistic Regression vs Naive Bayes Aspect Logistic Regression Naive Bayes Model type Discriminative models
      P Y X Generative models P X Y and P Y Main approach Learns coefficients by optimizing a loss function
      Estimates priors and likelihoods from training data Feature assumption No conditional independence
      assumption is required Uses a conditional independence assumption in its standard form Output Class
      probabilities and labels Class probabilities and labels Useful when A flexible linear decision boundary
      and interpretable coefficients are useful Training data are limited or conditional feature distributions
      are reasonably modeled

## Confusion matrix

**المصادر القديمة:** DM_Week5_Confusion_Matrix (archive).pptx.  **مصادر 2026:** Week6_Classification.docx.

**الكلمات المرمّزة:** القديم 1,363؛ الحالي 3,020؛ المتطابق بالترتيب 87. The archive is 27 slides; compare its text with current Week 6.

1. − OLD [1–6]:
   Data Mining Week5 What is a
   + 2026 [1–1246]:
      Classification in Data Mining 1 Introduction to Classification 1 1 Definition of Classification
      Classification is one of the most important techniques in Data Mining and Machine Learning It is used to
      assign a data record to one of a set of predefined classes Simple Definition Classification is the process
      of learning from previously labeled data and using the learned knowledge to assign a class to new data For
      example a hospital may want to determine whether a patient has a particular disease The possible classes
      could be Disease No Disease The classification model learns from previous patients and then predicts the
      class of a new patient 1 2 Why Classification Is Important Classification is important because many real
      world problems require us to make decisions based on available data For example Healthcare Predict whether
      a patient has a disease Banking Predict whether a customer is likely to default on a loan Education
      Predict whether a student will pass or fail Cybersecurity Determine whether network traffic is normal or
      malicious Email Determine whether an email is spam or not spam Business Predict whether a customer will
      leave a company Therefore classification is widely used for prediction and decision making 1 3
      Classification as Supervised Learning Classification is a type of supervised learning The term supervised
      means that the training data contains the correct answers For example consider a dataset containing
      patient information Age Glucose BMI Diabetes 25 110 23 5 No 45 180 31 2 Yes 52 160 29 8 Yes 30 95 22 1 No
      The first three columns describe the patients The last column contains the known class The algorithm
      studies these examples and learns patterns that can be used to classify new patients Basic Idea Labeled
      Data Classification Algorithm Classification Model New Data Predicted Class 1 4 Applications of
      Classification Classification is used in many areas Medical Applications Disease diagnosis Cancer
      classification Patient risk classification Financial Applications Fraud detection Credit risk
      classification Loan approval Educational Applications Student performance prediction Student dropout
      prediction Pass and fail prediction Cybersecurity Applications Malware classification Intrusion detection
      Phishing detection Business Applications Customer churn prediction Customer response prediction Product
      classification Text Mining Applications Spam detection Sentiment classification Document classification
      Image Applications Object classification Face recognition Medical image classification 2 Basic Concepts of
      Classification Before studying classification algorithms students need to understand several important
      terms 2 1 Dataset A dataset is a collection of data records For example a medical dataset may contain
      information about thousands of patients A student dataset may contain information about Student age
      Attendance Grades Study hours Final result 2 2 Instance An instance is one individual record in a dataset
      For example One patient is one instance One student is one instance One email is one instance In a table
      an instance is usually represented by one row 2 3 Feature A feature is an attribute that describes an
      instance For example patient features may include Age Weight Blood pressure Glucose BMI Features are also
      called Attributes Variables Predictors Features are used by the classification model to make predictions 2
      4 Class Label The class label is the category that we want to predict Examples Diabetes Yes No Cancer
      Benign Malignant Student Performance Pass Fail Email Spam Not Spam The class label is also commonly called
      the target variable 2 5 Training Data Training data is the data used to teach the classification algorithm
      It contains Features Known class labels The algorithm examines the training data and learns patterns 2 6
      Validation Data Validation data is used during model development It can help us Select between different
      models Tune model settings Detect overfitting Choose the best model Validation data is particularly useful
      when developing more complex models 2 7 Test Data Test data is used to evaluate the final classification
      model The model should not use the test data during training The purpose is to determine how well the
      model performs on unseen data 3 How Classification Works Classification normally involves several stages 3
      1 Model Training First we provide the algorithm with training data For example Study Hours Attendance
      Previous Grade Result 2 60 50 Fail 4 75 65 Pass 6 90 80 Pass 1 50 40 Fail 5 85 75 Pass The algorithm
      examines the relationship between the features and the class It tries to learn patterns that distinguish
      one class from another 3 2 Model Testing After training the model is evaluated using data that it has not
      seen during training For example Study Hours Attendance Previous Grade Actual Result 3 70 55 Fail 6 88 82
      Pass The model predicts the results We then compare the predictions with the actual results 3 3
      Classification of New Data Once we are satisfied with the model's performance we can use it to classify
      new records For example New student Study hours 5 Attendance 88 percent Previous grade 78 The model may
      predict Pass The model made this prediction based on patterns learned from previous students 3 4 Example
      of a Classification Problem Consider a hospital that wants to classify patients into High Risk Low Risk
      The hospital has historical patient data Features may include Age Blood pressure Cholesterol Weight
      Previous medical history The model learns from previous patients When a new patient arrives the model
      predicts High Risk or Low Risk 4 Types of Classification There are several types of classification
      problems 4 1 Binary Classification Binary classification contains two classes Examples Email Spam Not Spam
      Medical Diagnosis Disease No Disease Education Pass Fail Banking Fraud Not Fraud Binary classification is
      one of the most common types of classification 4 2 Multiclass Classification Multiclass classification
      contains more than two classes For example an image classification system may classify images into Cat Dog
      Horse Bird Another example is disease classification Diabetes Heart Disease Kidney Disease Healthy The
      model normally assigns one class to each instance 4 3 Multilabel Classification In multilabel
      classification one instance can belong to more than one class at the same time For example a research
      paper could be classified as Artificial Intelligence Machine Learning Data Mining The paper can belong to
      all three categories Difference Multiclass One instance One class Multilabel One instance Multiple classes
      4 4 Classification and Regression Classification and regression are both supervised learning techniques
      but they predict different types of outputs Classification Predicts a category Example Patient Disease or
      No Disease Regression Predicts a numerical value Example Patient Expected blood glucose level Therefore
      Classification predicts categories while regression predicts numerical values 4 5 Classification and
      Clustering Classification and clustering are often confused They are different techniques Classification
      Clustering Supervised learning Unsupervised learning Uses labeled data Uses unlabeled data Classes are
      already known Groups are discovered Used for prediction Used to discover patterns Example If we know that
      emails are Spam Not Spam and we train a model to classify new emails this is classification If we have
      thousands of emails without labels and want to discover groups of similar emails this is clustering 5
      Classification Algorithms There are many classification algorithms The most important algorithms include
      Decision Tree Naive Bayes K Nearest Neighbors Support Vector Machine Logistic Regression Random Forest
      Neural Networks 6 Classification Model Evaluation After building a classification model we need to
      determine how well it performs Model evaluation is important because a model that performs well on
      training data may not necessarily perform well on new data Important evaluation measures include Confusion
      Matrix Accuracy Precision Recall Specificity F1 score ROC Curve AUC 6 1
2. − OLD [12–144]:
   is an N x N matrix used for evaluating the performance of a classification model where N is the number of
   target classes The matrix compares the actual target values with those predicted by the classification model
   confusion matrix A good model is one which has high TP and TN rates while low FP and FN rates If you have an
   imbalanced dataset to work with it’s always better to use confusion matrix as your evaluation criteria for
   your machine learning model Imbalanced data refers to those types of datasets where the target class has an
   uneven distribution of observations i e one class label has a very high number of observations and the other
   has a very low number of observations A confusion matrix is a tabular summary of the number of
   + 2026 [1252–1253]:
      shows the
3. − OLD [152–1363]:
   classifier It is used to measure the performance of a classification model It can be used to evaluate the
   performance of a classification model through the calculation of performance metrics like accuracy precision
   recall and F1 score We can measure model accuracy by two methods Accuracy simply means the number of values
   correctly predicted 1 Confusion Matrix 2 Classification Measure 1 Confusion Matrix The following 4 are the
   basic terminology which will help us in determining the metrics we are looking for True Positives TP when the
   actual value is Positive and predicted is also Positive True negatives TN when the actual value is Negative
   and prediction is also Negative False positives FP When the actual is negative but prediction is Positive
   Also known as the Type 1 error False negatives FN When the actual is Positive but the prediction is Negative
   Also known as the Type 2 error For a binary classification problem we would have a 2 x 2 matrix as shown
   below with 4 values The target variable has two values Positive or Negative The columns represent the actual
   values of the target variable The rows represent the predicted values of the target variable b Understanding
   Confusion Matrix in an easier way Let’s take an example We have a total of 20 cats and dogs and our model
   predicts whether it is a cat or not Actual values dog cat dog cat dog dog cat dog cat dog dog dog dog cat dog
   dog cat dog dog cat Predicted values dog dog dog cat dog dog cat cat cat cat dog dog dog cat dog dog cat dog
   dog cat True Positive TP 6 You predicted positive and it’s true You predicted that an animal is a cat and it
   actually is True Negative TN 11 You predicted negative and it’s true You predicted that animal is not a cat
   and it actually is not it’s a dog False Positive Type 1 Error FP 2 You predicted positive and it’s false You
   predicted that animal is a cat but it actually is not it’s a dog False Negative Type 2 Error FN 1 You
   predicted negative and it’s false You predicted that animal is not a cat but it actually is 2 Classification
   Measure Basically it is an extended version of the confusion matrix There are measures other than the
   confusion matrix which can help achieve better understanding and analysis of our model and its performance a
   Accuracy b Precision c Recall TPR Sensitivity d F1 Score e FPR Type I Error f FNR Type II Error Accuracy
   Accuracy simply measures how often the classifier makes the correct prediction It’s the ratio between the
   number of correct predictions and the total number of predictions The accuracy metric is not suited for
   imbalanced classes Accuracy has its own disadvantages for imbalanced data when the model predicts that each
   point belongs to the majority class label the accuracy will be high But the model is not accurate It is a
   measure of correctness that is achieved in true prediction In simple words it tells us how many predictions
   are actually positive out of all the total positive predicted Accuracy is a valid choice of evaluation for
   classification problems which are well balanced and not skewed or there is no class imbalance Precision It is
   a measure of correctness that is achieved in true prediction In simple words it tells us how many predictions
   are actually positive out of all the total positive predicted Precision is defined as the ratio of the total
   number of correctly classified positive classes divided by the total number of predicted positive classes Or
   out of all the predictive positive classes how much we predicted correctly Precision should be high ideally 1
   Precision is a useful metric in cases where False Positive is a higher concern than False Negatives Ex 1 In
   Spam Detection Need to focus on precision Suppose mail is not a spam but model is predicted as spam FP False
   Positive We always try to reduce FP Ex 2 Precision is important in music or video recommendation systems e
   commerce websites etc Wrong results could lead to customer churn and be harmful to the business Recall It is
   a measure of actual observations which are predicted correctly i e how many observations of positive class
   are actually predicted as positive It is also known as Sensitivity Recall is a valid choice of evaluation
   metric when we want to capture as many positives as possible Recall is defined as the ratio of the total
   number of correctly classified positive classes divide by the total number of positive classes Or out of all
   the positive classes how much we have predicted correctly Recall should be high ideally 1 Recall is a useful
   metric in cases where False Negative trumps False Positive Ex 1 suppose person having cancer or not He is
   suffering from cancer but model predicted as not suffering from cancer Ex 2 Recall is important in medical
   cases where it doesn’t matter whether we raise a false alarm but the actual positive cases should not go
   undetected Recall would be a better metric because we don’t want to accidentally discharge an infected person
   and let them mix with the healthy population thereby spreading contagious virus Now you can understand why
   accuracy was a bad metric for our model Trick to remember Precision has Predictive Results in the denominator
   F measure F1 Score The F1 score is a number between 0 and 1 and is the harmonic mean of precision and recall
   We use harmonic mean because it is not sensitive to extremely large values unlike simple averages F1 score
   sort of maintains a balance between the precision and recall for your classifier If your precision is low the
   F1 is low and if the recall is low again your F1 score is low There will be cases where there is no clear
   distinction between whether Precision is more important or Recall We combine them In practice when we try to
   increase the precision of our model the recall goes down and vice versa The F1 score captures both the trends
   in a single value F1 score is a harmonic mean of Precision and Recall As compared to Arithmetic Mean Harmonic
   Mean punishes the extreme values more F score should be high ideally 1 Sensitivity Specificity Is it
   necessary to check for recall or precision if you already have a high accuracy We can not rely on a single
   value of accuracy in classification when the classes are imbalanced For example we have a dataset of 100
   patients in which 5 have diabetes and 95 are healthy However if our model only predicts the majority class i
   e all 100 people are healthy even though we have a classification accuracy of 95 When to use Accuracy
   Precision Recall F1 Score a Accuracy is used when the True Positives and True Negatives are more important
   Accuracy is a better metric for Balanced Data b Whenever False Positive is much more important use Precision
   c Whenever False Negative is much more important use Recall d F1 Score is used when the False Negatives and
   False Positives are important F1 Score is a better metric for Imbalanced Data
   + 2026 [1261–3020]:
      classification model For binary classification Predicted Positive Predicted Negative Actual Positive True
      Positive False Negative Actual Negative False Positive True Negative 6 2 True Positive The actual class is
      positive The model also predicts positive Example A patient has cancer The model predicts cancer This is a
      True Positive 6 3 True Negative The actual class is negative The model also predicts negative Example A
      patient does not have cancer The model predicts no cancer This is a True Negative 6 4 False Positive The
      actual class is negative The model predicts positive Example A patient does not have cancer The model
      predicts cancer This is a False Positive This can be considered a false alarm 6 5 False Negative The
      actual class is positive The model predicts negative Example A patient has cancer The model predicts no
      cancer This is a False Negative In some medical applications false negatives can be particularly serious 6
      6 Accuracy Accuracy measures the percentage of all predictions that are correct For example Suppose there
      are 100 patients The model correctly classifies 95 patients The accuracy is 95 percent Accuracy is easy to
      understand but it should not always be used alone 6 7 Precision Precision answers the question When the
      model predicts positive how often is it correct Formulas For example The model predicts that 100 patients
      have a disease Only 90 actually have the disease The precision is 90 percent Precision is important when
      false positive predictions are costly 6 8 Recall Recall answers the question Of all the cases that are
      actually positive how many did the model correctly identify For example There are 100 patients who
      actually have a disease The model correctly identifies 95 of them The recall is 95 percent Recall is
      especially important when missing a positive case can have serious consequences 6 9 Specificity
      Specificity answers the question Of all the cases that are actually negative how many did the model
      correctly identify For example There are 100 healthy patients The model correctly identifies 90 of them as
      healthy The specificity is 90 percent 6 10 F1 Score F1 score combines precision and recall into one
      measure It is particularly useful when The dataset is imbalanced Both false positives and false negatives
      are important A high F1 score means that the model has a good balance between precision and recall 6 11
      ROC Curve The ROC curve is used mainly for binary classification It evaluates the model at different
      decision thresholds It considers two important aspects How well the model identifies positive cases How
      often the model incorrectly identifies negative cases as positive A model with better separation between
      the classes generally has a better ROC curve 6 12 AUC AUC means Area Under the ROC Curve It provides a
      single value that summarizes the model's ability to distinguish between classes Generally AUC General
      Interpretation 0 50 Random performance 0 60 0 70 Poor 0 70 0 80 Acceptable 0 80 0 90 Good 0 90 1 00
      Excellent These values should be considered general guidelines rather than strict rules 7 Problems in
      Classification Classification models can face several problems The most important are Class imbalance
      Overfitting Underfitting Irrelevant features Missing data Noisy data 7 1 Class Imbalance Class imbalance
      occurs when one class contains significantly more records than another For example Class Number Healthy 9
      000 Disease 1 000 The dataset is imbalanced Suppose a model predicts every patient as healthy The model
      would achieve 90 percent accuracy However it would fail to identify any patient with the disease Therefore
      High accuracy does not always mean that a classification model is good 7 2 Overfitting Overfitting occurs
      when the model learns the training data too closely For example Training accuracy 99 percent Testing
      accuracy 70 percent The large difference suggests that the model may have learned the training data rather
      than learning general patterns Causes Model is too complex Dataset is too small Too many features Noisy
      data Insufficient regularization 7 3 Underfitting Underfitting occurs when the model is too simple to
      learn the important patterns in the data For example Training accuracy 65 percent Testing accuracy 63
      percent The model performs poorly on both training and testing data Possible solutions include Using a
      more appropriate algorithm Adding useful features Reducing excessive regularization Improving the quality
      of the data 7 4 Irrelevant Features Not every feature in a dataset is useful For example suppose we want
      to predict whether a patient has diabetes Useful features may include Age Glucose BMI Blood pressure An
      unrelated feature may add noise without helping the prediction Too many irrelevant features can Increase
      complexity Increase training time Reduce model performance Increase the risk of overfitting 7 5 Missing
      Data Real world datasets often contain missing values For example Age Glucose BMI 45 180 31 52 Missing 29
      30 95 22 Missing data must be handled appropriately before training many classification models Possible
      approaches include Removing records Replacing missing values Using statistical imputation Using model
      based imputation The appropriate approach depends on the dataset and the reason for the missing values 7 6
      Noisy Data Noise refers to incorrect inconsistent or unnecessary information in the dataset Examples
      include Incorrect measurements Typographical errors Incorrect labels Extreme values caused by measurement
      errors Data cleaning is an important step before classification 8 Improving Classification Performance
      Several techniques can improve classification performance 8 1 Data Preprocessing Data preprocessing
      prepares the dataset before model training It may include Handling missing values Removing duplicates
      Correcting errors Encoding categorical data Scaling numerical features Good preprocessing can
      significantly affect model performance 8 2 Feature Selection Feature selection means choosing the most
      useful features Suppose a dataset contains 100 features Only 20 may be strongly related to the target
      class Using the most useful features can Reduce complexity Reduce training time Reduce overfitting Improve
      interpretability Sometimes improve prediction performance Common techniques include Information Gain Chi
      Square Correlation Mutual Information Recursive Feature Elimination Feature Importance 8 3 Feature Scaling
      Feature scaling ensures that numerical features have comparable scales For example Age may range from 18
      to 80 Income may range from 1 000 to 100 000 The large difference in scale can affect algorithms such as
      KNN SVM Logistic Regression Neural Networks Common scaling methods include Standardization Min Max Scaling
      Robust Scaling 8 4 Handling Class Imbalance Several techniques can be used Oversampling Increase the
      number of minority class examples Undersampling Reduce the number of majority class examples SMOTE SMOTE
      creates synthetic examples for the minority class Class Weights Give greater importance to minority class
      errors Appropriate Evaluation Measures Use Precision Recall F1 score Specificity AUC rather than relying
      only on accuracy 8 5 Cross Validation Cross validation is used to obtain a more reliable estimate of model
      performance In five fold cross validation the dataset is divided into five parts The model is trained and
      evaluated several times Each part is used as the validation set while the remaining parts are used for
      training The results are then averaged Cross validation is especially useful when the available dataset is
      not very large 8 6 Hyperparameter Tuning Classification algorithms contain settings called hyperparameters
      Examples include KNN Number of neighbors Decision Tree Maximum tree depth Random Forest Number of trees
      SVM Kernel and other model settings Hyperparameter tuning attempts to find suitable values for these
      settings Common methods include Grid Search Random Search Bayesian Optimization 8 7 Ensemble Methods An
      ensemble method combines multiple models to produce a stronger prediction Examples include Random Forest
      Gradient Boosting AdaBoost XGBoost The main idea is that combining several models can sometimes produce
      better and more stable results than using one model alone 9 Classification Workflow A complete
      classification project normally follows a sequence of steps Step 1 Data Collection Collect the required
      dataset Step 2 Data Understanding Study Number of records Features Classes Data types Class distribution
      Step 3 Data Cleaning Handle Missing values Duplicate records Incorrect values Noise Step 4 Data
      Preparation Perform appropriate Encoding Scaling Transformation Step 5 Feature Selection Select useful
      features Step 6 Data Splitting Divide the data into appropriate training validation and testing sets Step
      7 Model Training Train one or more classification algorithms Step 8 Model Evaluation Evaluate the models
      using appropriate performance measures Step 9 Model Tuning Improve the selected model by tuning its
      hyperparameters Step 10 Final Prediction Use the final model to classify new unseen data 10 Comparison of
      Classification Algorithms Algorithm Main Strength Main Weakness Decision Tree Easy to understand Can
      overfit Naive Bayes Fast and simple Strong independence assumption KNN Simple and intuitive Can be slow
      with large datasets SVM Good for complex boundaries Can require careful parameter tuning Logistic
      Regression Simple and interpretable Limited for complex relationships Random Forest Robust and accurate
      Less interpretable Neural Network Powerful for complex data Requires careful training There is no single
      classification algorithm that is best for every dataset The best choice depends on Dataset size Number of
      features Data type Class distribution Complexity of the problem Required interpretability Computational
      resources 11 Applications of Classification Classification has many real world applications 11 1
      Healthcare Examples Disease diagnosis Cancer classification Patient risk prediction Medical image
      classification 11 2 Banking and Finance Examples Fraud detection Loan approval Credit risk classification
      Customer risk assessment 11 3 Education Examples Student performance prediction Dropout prediction Pass
      and fail prediction Student risk classification 11 4 Cybersecurity Examples Intrusion detection Malware
      classification Phishing detection Network traffic classification 11 5 Business Examples Customer churn
      prediction Customer response prediction Product classification Customer risk classification 11 6 Text
      Mining Examples Spam detection Sentiment analysis News classification Document classification 11 7 Image
      Classification Examples Face recognition Object classification Medical image classification Animal
      classification 12 Practical Classification Example Breast Cancer Classification Consider a breast cancer
      dataset The dataset contains information about breast tumors Features Examples include Tumor size Cell
      characteristics Texture Shape Other medical measurements Classes The target class may be Benign Malignant
      Practical Process Step 1 Load the dataset Step 2 Examine the features and classes Step 3 Check for missing
      values Step 4 Check whether the classes are balanced Step 5 Prepare the features Step 6 Divide the data
      into training and testing sets Step 7 Train several classification algorithms Logistic Regression Decision
      Tree KNN SVM Random Forest Step 8 Evaluate each model Use Accuracy Precision Recall Specificity F1 score
      AUC Step 9 Compare the results Step 10 Select the most appropriate model The best model should not
      necessarily be the model with the highest accuracy For a medical application recall and specificity may be
      particularly important

## Clustering overview

**المصادر القديمة:** DM_Clustering_Supervised_Unsupervised (archive).docx.  **مصادر 2026:** Week8_Clustering.pdf.

**الكلمات المرمّزة:** القديم 1,942؛ الحالي 2,912؛ المتطابق بالترتيب 325. Direct overview-to-week comparison; handwritten/examples are inventoried in the main audit instead of OCR word alignment.

1. − OLD [1–150]:
   supervised and unsupervised Supervised Learning Definition A type of machine learning where the model is
   trained using a dataset that contains both input features and labeled outputs Goal Learn the mapping between
   inputs and outputs so the model can predict outcomes for new data Example Input Features of houses size
   location number of rooms Output label House price Task Train the model to predict house prices Algorithms
   Linear Regression Logistic Regression Decision Trees Random Forest Support Vector Machines SVM Neural
   Networks Unsupervised Learning Definition A type of machine learning where the dataset contains only input
   features with no labeled outputs The model tries to find hidden patterns or structures in the data Goal
   Discover natural groupings structures or representations of data Example Input Customer purchase data no
   labels Task Group customers into segments with similar buying behavior Algorithms K Means Clustering DBSCAN
   Hierarchical Clustering Principal Component Analysis PCA Key Differences
   + 2026 [1–279]:
      DATA MINING WEEK 8 Week 8 Clustering WEEK 8 CLUSTERING Clustering as an Application of Data Mining 1
      Introduction to Data Mining Data Mining is the process of discovering useful patterns relationships trends
      and knowledge from large amounts of data It uses techniques from statistics machine learning databases and
      artificial intelligence to analyze data and support decision making The main purpose of Data Mining is not
      simply to store or retrieve data Its purpose is to discover information that may not be immediately
      obvious from the original data 1 1 Example of Data Mining A university may collect information about
      students such as attendance study hours assignment marks and examination results Data Mining techniques
      can analyze these records to discover patterns identify students who may need support or group students
      with similar academic behavior 1 2 Main Tasks of Data Mining Data Mining Task Purpose Example
      Classification Assign an item to one of several predefined categories Classify an email as spam or not
      spam Prediction Regression Estimate a numerical value or a future outcome Predict a student's final mark
      Clustering Group similar data items without predefined class labels Group students according to academic
      behavior Association Rule Mining Discover items or events that frequently occur together Find products
      commonly purchased together Anomaly Detection Identify unusual patterns or observations Detect unusual
      banking transactions Summarization Provide a compact description of a dataset Summarize customer
      characteristics Remember Classification asks Which known category does this record belong to Clustering
      asks Which records are similar to one another 2 Supervised and Unsupervised Learning Machine learning
      methods are commonly divided into supervised learning and unsupervised learning according to whether the
      training data contain known target labels
2. − OLD [156–222]:
   Data Labeled input output Unlabeled only input Goal Predict outcomes Find hidden patterns Examples
   Classification Regression Clustering Dimensionality Reduction Algorithms Regression Decision Trees Neural
   Networks K Means DBSCAN PCA Real world Use Spam detection credit scoring Customer segmentation image grouping
   In short Supervised Learning Learn from labeled examples to make predictions Unsupervised Learning Find
   hidden structures in unlabeled data What Is Cluster Analysis Cluster analysis is a
   + 2026 [285–645]:
      Training data Contains input features and known labels Contains input features without target labels Main
      purpose Learn to predict a known target Discover hidden structures or patterns Typical tasks
      Classification and regression Clustering and dimensionality reduction Example Predict whether a
      transaction is fraudulent using labeled examples Group transactions with similar behavior without labels
      DATA MINING WEEK 8 Week 8 Clustering For example if student records already contain labels such as
      Excellent Good and Needs Support a model can learn to predict those labels This is supervised learning If
      labels are not provided and an algorithm discovers groups of similar students this is unsupervised
      learning 3 Clustering as an Application of Data Mining Clustering is an important Data Mining task It
      divides a dataset into groups called clusters so that data objects in the same group are more similar to
      one another than to objects in other groups Unlike classification clustering does not require predefined
      class labels The algorithm examines the data and attempts to discover groups based on similarities or
      distances between objects 3 1 University Example Suppose a university has records for 500 students Each
      record contains attendance percentage weekly study hours assignment score and examination score The
      university does not provide predefined student categories A clustering algorithm may discover groups such
      as Cluster 1 students with high attendance high study hours and high marks Cluster 2 students with
      moderate attendance and moderate marks Cluster 3 students with low attendance and low marks These group
      descriptions are interpretations made after examining the clusters The algorithm itself discovers groups
      from the data it does not automatically know the educational meaning of each group 3 2 Relationship
      Between Data Mining Machine Learning and Clustering Concept Meaning Data Mining A broader process of
      discovering useful patterns and knowledge from data Machine Learning A set of computational methods that
      learn patterns from data Unsupervised Learning A machine learning approach that works with data without
      target labels Clustering A common unsupervised learning task used to group similar data objects K Means
      DBSCAN Hierarchical Algorithms that perform clustering in different ways Therefore clustering is a Data
      Mining task and is commonly performed using unsupervised learning algorithms
3. − OLD [228–245]:
   technique used to group a set of objects into clusters groups so that Objects within the same cluster
   + 2026 [651–1309]:
      are related but they are not identical terms 4 Introduction to Clustering Clustering is the process of
      organizing a collection of data objects into groups based on their similarity Each group is called a
      cluster Objects in the same cluster should be relatively similar while objects in different clusters
      should be relatively dissimilar 4 1 Main Objectives of Clustering Discover natural groups or structures in
      data Understand the characteristics of different groups Summarize large datasets using a smaller number of
      groups Identify unusual objects that do not fit well into any group Support further analysis and decision
      making 4 2 Applications of Clustering Application Area Example Marketing Group customers according to
      purchasing behavior Healthcare Group patients according to similar clinical measurements DATA MINING WEEK
      8 Week 8 Clustering Education Group students according to learning or academic patterns Image Analysis
      Group pixels or image regions with similar properties Cybersecurity Group network activities and
      investigate unusual groups Document Analysis Group scientific papers according to their content 5
      Similarity and Distance Measures Clustering algorithms need a way to compare data objects A distance
      measure indicates how far apart two objects are A similarity measure indicates how alike they are The
      appropriate measure depends on the type of data and the clustering algorithm 5 1 Euclidean Distance
      Euclidean distance is the straight line distance between two points For two points A x y and B x y the
      formula is d A B x x y y Example Let A 2 3 and B 5 7 d A B 5 2 7 3 3 4 9 16 25 5 The Euclidean distance
      between A and B is 5 A smaller distance means the points are closer 5 2 Manhattan Distance Manhattan
      distance is the sum of the absolute differences between corresponding coordinates d A B x x y y Using A 2
      3 and B 5 7 d A B 5 2 7 3 3 4 7 5 3 Cosine Similarity Cosine Similarity measures the angle between two
      vectors It is often useful for text data because it compares vector direction rather than their absolute
      magnitudes Cosine Similarity A B A B A B Its common range is from 1 to 1 For non negative text vectors
      values are usually between 0 and 1 A value closer to 1 indicates greater similarity Important Features
      measured on very different scales can dominate distance calculations For methods based on distance
      consider normalizing or standardizing numerical features 5 4 Worked Example Cosine Similarity in Document
      Clustering Suppose we have three documents and want to group them according to their content A text
      vectorization method converts each document into a numerical vector For this simplified example assume the
      following Document Content Vector A Data Mining and AI 1 1 0 B Data Mining and Machine Learning 1 1 1 C
      Football and Sports 0 0 2 DATA MINING WEEK 8 Week 8 Clustering Step 1 Calculate the similarity between
      Documents A and B First calculate the dot product A B 1 1 1 1 0 1 2 Next calculate the magnitude length of
      each vector A 1 1 0 2 B 1 1 1 3 Substitute these values into the Cosine Similarity formula Cosine A B 2 2
      3 2 2 449 0 816 Interpretation Documents A and B have relatively high similarity because their vectors
      point in similar directions Step 2 Calculate the similarity between Documents A and C Calculate the dot
      product A C 1 0 1 0 0 2 0 Calculate the magnitudes A 2 C 0 0 2 2 Apply the formula Cosine A C 0 2 2 0
      Interpretation Documents A and C have no directional similarity in this simplified example Step 3 Compare
      the similarity values Document Pair Cosine Similarity Interpretation A and B 0 816 Relatively high
      similarity A and C 0 000 No directional similarity Step 4 Form possible clusters Based on the similarity
      values Documents A and B
4. − OLD [252–504]:
   high intra cluster similarity Objects in different clusters are more dissimilar low inter cluster similarity
   It is an unsupervised learning method meaning the data has no predefined labels or categories the algorithm
   finds patterns and structures on its own Key Points about Cluster Analysis Purpose To discover natural
   groupings or structures in data without prior knowledge Applications Customer segmentation in marketing
   Grouping patients with similar symptoms in healthcare Image segmentation in computer vision Document or news
   article clustering in text mining Methods Partitioning methods e g k means k medoids Hierarchical methods e g
   agglomerative divisive Density based methods e g DBSCAN Model based methods e g Gaussian Mixture Models
   Similarity Measures To decide how close objects are measures like Euclidean distance cosine similarity or
   Manhattan distance are commonly used In short cluster analysis helps in identifying patterns structures or
   groups in data when labels are not available Why is Clustering Important Clustering helps in exploring and
   understanding data especially when we don’t know the categories in advance It is often used as a first step
   in data analysis to reveal hidden patterns What are Partitioning Methods Partitioning methods are clustering
   techniques that divide a dataset into a fixed number of clusters k where each object belongs to exactly one
   cluster The most common example is K Means clustering The idea is simple Define how many clusters you want k
   Assign each data point to the closest cluster Adjust cluster centers until the grouping is stable How
   Partitioning Methods Work Step by Step
   + 2026 [1316–1518]:
      while Document C is different from them A possible grouping is Cluster Documents Description Cluster 1 A
      and B Technology related documents Cluster 2 C Sports related document The cluster descriptions are
      assigned by a person after examining the documents The similarity calculation compares the numerical
      representations it does not automatically assign meaningful labels Converting Cosine Similarity into
      Cosine Distance Some clustering methods use a distance value rather than a similarity value A simple
      cosine distance is DATA MINING WEEK 8 Week 8 Clustering Cosine Distance 1 Cosine Similarity For Documents
      A and B Cosine Distance A B 1 0 816 0 184 A smaller cosine distance indicates greater similarity Cosine
      Similarity is a similarity measure not a clustering algorithm It can be used with suitable clustering
      methods such as hierarchical clustering 6 Main Types of Clustering Algorithms Clustering algorithms use
      different strategies to form groups This lecture introduces four common families partitioning hierarchical
      density based and model based clustering 6 1 Partitioning Clustering K Means K Means is a partitioning
      algorithm that divides a dataset into K clusters Each cluster is represented by its centroid which is the
      mean position of the objects assigned to that cluster How K Means Works 1
5. − OLD [511–556]:
   The user decides how many clusters they want Initialize cluster centers Select k points randomly from the
   dataset as initial centroids cluster centers Assign points to the nearest cluster For each data point
   calculate the distance e g Euclidean distance to each centroid Assign the point
   + 2026 [1525–1554]:
      2 Initialize K centroids The initial centroids may be selected randomly or using K Means 3 Calculate the
      distance from each data object to each centroid 4 Assign each object
6. − OLD [564–862]:
   Update cluster centers Recalculate the centroid of each cluster usually the mean of the points in the cluster
   Repeat until convergence Keep assigning points and updating centroids until clusters no longer change
   significantly or a maximum number of iterations is reached Example K Means Suppose we want to cluster
   students based on study hours and exam scores into 2 groups Initialize two centroids randomly Assign each
   student to the nearest centroid group Update the centroids based on the average of each group Repeat until
   the groups stop changing Advantages of Partitioning Methods Easy to understand and implement Works well with
   large datasets Fast compared to hierarchical clustering Limitations Must specify k in advance Sensitive to
   initial centroid selection Works best with spherical well separated clusters What are Hierarchical Methods
   Hierarchical clustering is a clustering technique that builds a tree like structure dendrogram to represent
   how data points are grouped together at different levels of similarity Unlike K Means or K Medoids you don’t
   need to predefine k the number of clusters You can cut the dendrogram at different levels to get different
   numbers of clusters Types of Hierarchical Clustering Agglomerative Bottom Up Start with each data point as
   its own cluster At each step merge the two closest clusters until only one cluster remains the root Most
   commonly used Divisive Top Down Start with one big cluster containing all data points At each step split the
   cluster into smaller ones Continue until each point is its own cluster How Agglomerative Hierarchical
   Clustering Works Step by Step Start Each data point is a separate cluster Compute distances between all
   clusters using metrics like Euclidean distance Manhattan distance or cosine similarity Merge the closest two
   clusters Recompute distances between the new cluster and all other clusters Different methods to calculate
   distance
   + 2026 [1562–1887]:
      5 Recalculate each centroid as the mean of the objects assigned to its cluster 6 Repeat the assignment and
      centroid update steps until the assignments or centroids stop changing significantly Simple Example
      Suppose the one dimensional data values are 2 4 10 and 12 and K 2 If the initial centroids are 2 and 10
      the nearest centroid assignments are Data Point Distance to Centroid 2 Distance to Centroid 10 Assigned
      Cluster 2 0 8 Cluster 1 4 2 6 Cluster 1 10 8 0 Cluster 2 12 10 2 Cluster 2 The new centroid of Cluster 1
      is 2 4 2 3 The new centroid of Cluster 2 is 10 12 2 11 The algorithm repeats the process using these
      updated centroids Advantages of K Means Simple to understand and implement Efficient for many numerical
      datasets Works well when clusters are compact and reasonably separated Limitations of K Means The value of
      K must be selected in advance Results can depend on the initial centroids It is sensitive to outliers and
      feature scaling It may perform poorly when clusters have irregular shapes or very different densities DATA
      MINING WEEK 8 Week 8 Clustering K Means Initialization K Means is an initialization method designed to
      choose starting centroids that are spread out It generally reduces the chance of selecting poor initial
      centroids It does not change the basic assignment and centroid update steps of K Means 6 2 Hierarchical
      Clustering Hierarchical clustering creates a hierarchy of clusters Its result is commonly represented
      using a tree like diagram called a dendrogram Two Main Approaches Approach Description Agglomerative
      bottom up Starts with each object as its own cluster and repeatedly merges the closest clusters Divisive
      top down Starts with all objects in one cluster and repeatedly splits clusters into smaller groups Linkage
      Methods When two clusters contain multiple objects a linkage method defines how the distance between the
      clusters is calculated Linkage Method How Cluster Distance Is Calculated
7. − OLD [868–871]:
   points in two clusters
   + 2026 [1893–1900]:
      any pair of objects one from each cluster
8. − OLD [877–1169]:
   points in two clusters Average linkage average distance between points in two clusters Centroid linkage
   distance between centroids Repeat steps 3 4 until only one cluster remains The result is a dendrogram By
   cutting the dendrogram at a chosen height you decide the number of clusters Example Suppose we have 5
   students with study hours and exam scores Start Each student is its own cluster A B C D E Merge the two
   closest say A B Now we have AB C D E Next merge C with D if they are closest Continue until all are merged
   into one cluster The dendrogram shows this step by step merging If we cut the dendrogram in the middle we
   might get 2 clusters A B low study low score C D E high study high score Advantages of Hierarchical
   Clustering No need to predefine the number of clusters unlike K Means Produces a dendrogram which gives
   insight into the data’s structure Works well for small to medium sized datasets Limitations Computationally
   expensive for very large datasets O n Once a merge or split is done it cannot be undone greedy approach
   Sensitive to choice of distance metric and linkage method In short Hierarchical clustering builds a tree of
   clusters by either merging agglomerative or splitting divisive It’s widely used when you want to understand
   the nested grouping structure of data What are Density Based Methods Density based clustering groups data
   points into clusters based on the idea of density A cluster is formed where data points are densely packed
   together Areas with low density are treated as noise outliers Unlike K Means or Hierarchical clustering
   density based methods can find arbitrarily shaped clusters not just spherical The most famous density based
   algorithm is DBSCAN
   + 2026 [1906–2043]:
      any pair of objects one from each cluster Average linkage Average of the distances between all cross
      cluster object pairs Ward's method Merges clusters to minimize the increase in within cluster variance
      Dendrogram A dendrogram displays the sequence of merges or splits and the distances at which they occur To
      obtain a chosen number of clusters a horizontal cut can be made across the dendrogram The number of
      separate branches intersected by the cut determines the resulting clusters Advantages and Limitations
      Advantage the hierarchy can be examined at different levels of detail Advantage the number of clusters
      does not always need to be specified before building the hierarchy Limitation standard agglomerative
      methods can be computationally expensive for large datasets Limitation early merge or split decisions are
      generally not reversed 6 3 Density Based Clustering DBSCAN DBSCAN stands for
9. − OLD [1178–1195]:
   How DBSCAN Works DBSCAN uses two key parameters epsilon The maximum distance between two points to be
   considered
   + 2026 [2052–2082]:
      It forms clusters from dense regions of data and can identify isolated observations as noise Two Main
      Parameters Parameter Meaning Epsilon The maximum neighborhood distance used to decide which points are
10. − OLD [1202–1476]:
   neighbors within required to form a dense region cluster Steps Pick a point Find all points within distance
   neighbors If neighbors MinPts this is a core point and a new cluster starts If neighbors MinPts this point is
   noise unless it later becomes part of another cluster Expand the cluster by recursively adding all density
   connected points Repeat until all points are visited Example Simple Imagine we have data points representing
   customers shopping behavior Cluster 1 Many customers buy milk bread dense group Cluster 2 Many customers buy
   fruits vegetables dense group Some outliers Rare shoppers who buy very unusual items marked as noise DBSCAN
   will identify the two dense groups as clusters and ignore the outliers Advantages of Density Based Methods
   Can find arbitrarily shaped clusters not just round ones like K Means Automatically identifies outliers noise
   No need to predefine the number of clusters Limitations Choosing good values for and MinPts is tricky
   Struggles with datasets of varying densities one dense cluster one sparse cluster In short Density based
   methods like DBSCAN form clusters where data points are closely packed and separate them by low density areas
   They’re great for detecting arbitrary shapes and outliers in data Example Dataset 2D Points Suppose we have
   these points on a plane P1 1 2 P2 2 2 P3 2 3 P4 8 7 P5 8 8 P6 25 80 We choose 2 radius for neighbors MinPts 2
   minimum neighbors to form a cluster Step 1 Start with P1 1 2 Distance P1 P2 2 1 2 2 1 neighbor Distance P1 P3
   2 1 3 2 2 1 41 neighbor At least 2 neighbors P1
   + 2026 [2089–2247]:
      points required in the neighborhood for a point to be considered a core point DATA MINING WEEK 8 Week 8
      Clustering Counting convention In the common DBSCAN convention the point itself is included when counting
      the points in its neighborhood A course or software implementation should state its convention explicitly
      Types of Points Point Type Meaning Core point Has at least MinPts points in its neighborhood including
      itself under the common convention Border point Has fewer than MinPts points in its own neighborhood but
      lies within the neighborhood of a core point Noise point Is not a core point and is not density reachable
      from a core point Basic DBSCAN Procedure 7 Select an unvisited point 8 Find all points within its
      neighborhood 9 If it has fewer than MinPts points in its neighborhood mark it as noise temporarily It may
      later be identified as a border point if it is reached from a core point 10 If it
11. − OLD [1482–1632]:
   Cluster 1 Step 2 Expand Cluster 1 Add P2 and P3 because they are within Check P2 Its neighbors are P1 and P3
   enough core point Check P3 Its neighbors are P1 and P2 enough core point Cluster 1 P1 P2 P3 Step 3 Move to P4
   8 7 Distance P4 P5 8 8 8 7 1 neighbor Enough neighbors P4 is a core point start Cluster 2 Add P5 check its
   neighbors P4 also valid Cluster 2 P4 P5 Step 4 P6 25 80 No points within Not a core point not a border point
   Noise Outlier Final Clusters Cluster 1 P1 P2 P3 Cluster 2 P4 P5 Noise P6 This shows how DBSCAN works in
   practice Finds dense groups of points clusters Leaves isolated points as noise No need to specify the number
   of clusters beforehand What Are Model Based Methods Model based clustering assumes that the data is
   + 2026 [2253–2421]:
      a new cluster and expand the cluster through density reachable neighboring core points 11 Continue until
      all points have been visited Numerical Example Assume 2 and MinPts 4 with the point itself included in the
      count If point P has three other points within distance 2 its neighborhood contains four points in total
      Therefore P is a core point If point Q has only one other point within distance 2 its neighborhood
      contains two points in total Q is not a core point it may be a border point if it is within the
      neighborhood of a core point Otherwise it is noise Advantages and Limitations Can discover clusters with
      irregular shapes Can identify noise and outliers Does not require the number of clusters to be specified
      in advance Choosing suitable and MinPts values can be difficult A single density setting may not work well
      when clusters have very different densities 6 4 Model Based Clustering Gaussian Mixture Model GMM A
      Gaussian Mixture Model assumes that the data are
12. − OLD [1638–1652]:
   underlying probability distributions Each cluster corresponds to one probability distribution often Gaussian
   The algorithm tries
   + 2026 [2427–2507]:
      several Gaussian probability distributions Each Gaussian component represents one possible cluster Unlike
      K Means which assigns each object to one cluster GMM can provide a probability of membership for each
      object in each component This is called soft clustering Example A data object might have a 0 70
      probability of belonging to Component 1 and a 0 30 probability of belonging to Component 2 This expresses
      uncertainty about its cluster membership Expectation Maximization EM The Expectation Maximization
      algorithm is commonly used
13. − OLD [1658–1942]:
   these distributions mean variance mixing probability etc Then it assigns each point to the cluster
   distribution where it has the highest probability of belonging The most common model based method is the
   Gaussian Mixture Model GMM usually trained using the Expectation Maximization EM algorithm How Gaussian
   Mixture Models GMM Work Assume k clusters mixture components Each cluster is represented by a Gaussian
   distribution with its own mean center and covariance spread The EM algorithm is used E step Expectation
   Estimate the probability of each data point belonging to each Gaussian soft assignment M step Maximization
   Update the Gaussian parameters mean covariance and mixing weights to maximize likelihood Repeat until
   convergence Final assignment each point belongs to the cluster where it has the highest probability Example
   Simple Idea Suppose you measure people’s heights in a dataset The data may come from two groups men and women
   Instead of hard clustering like K Means a GMM fits two Gaussian curves one for men one for women Each person
   has a probability of belonging to each group So if someone’s height 170 cm Probability male 0 7 Probability
   female 0 3 GMM can keep this soft assignment instead of forcing a hard choice Advantages of Model Based
   Clustering Can model elliptical clusters unlike K Means which only works well with spherical clusters
   Provides probabilistic assignments soft clustering Handles overlapping clusters better Limitations You need
   to specify the number of clusters k in advance Can be computationally expensive for large datasets Sensitive
   to initial parameters In short Model based methods like GMM assume data comes from a mixture of probability
   distributions and use statistics to estimate clusters They’re powerful for soft clustering and for data that
   isn’t nicely separated
   + 2026 [2513–2912]:
      a GMM 12 Initialization choose initial parameters for the Gaussian components DATA MINING WEEK 8 Week 8
      Clustering 13 Expectation step E step estimate the probability that each data object belongs to each
      component 14 Maximization step M step update the component parameters using the estimated membership
      probabilities 15 Repeat the E step and M step until the model parameters or likelihood converge Important
      A Gaussian component is a mathematical component of the model It does not automatically correspond to a
      meaningful real world category interpretation requires examining the data 7 Determining the Number of
      Clusters Some clustering methods such as K Means require the number of clusters to be selected in advance
      Two commonly used evaluation approaches are the Elbow Method and the Silhouette Score 7 1 Elbow Method The
      Elbow Method runs K Means for several values of K and calculates the within cluster sum of squares WCSS
      for each value WCSS measures the sum of squared distances between data objects and the centroids of their
      assigned clusters Steps of the Elbow Method 16 Run K Means using K 1 2 3 and so on 17 Record the WCSS for
      each value of K 18 Plot K against WCSS 19 Look for a point where the decrease in WCSS begins to slow
      noticeably This point is called the elbow The elbow is a guide not a guaranteed mathematically optimal
      answer The choice should also consider the purpose of the analysis and whether the resulting clusters are
      useful 7 2 Silhouette Score The Silhouette Score measures how well an object fits within its assigned
      cluster compared with the nearest alternative cluster For an object i the Silhouette Score is s i b i a i
      max a i b i where a i is the average distance from object i to other objects in its own cluster and b i is
      the smallest average distance from object i to objects in another cluster the nearest neighboring cluster
      Silhouette Value Interpretation Close to 1 The object is well matched to its own cluster and separated
      from other clusters Around 0 The object is near a boundary between clusters Below 0 The object may be
      assigned to an unsuitable cluster The overall Silhouette Score is commonly calculated as the mean of the
      individual object scores A higher average score generally indicates better separated clusters but it
      should not be used alone

## Regression vs classification diagnostic comparison

**المصادر القديمة:** DM_Week11_Regression_vs_Classification (archive).docx.  **مصادر 2026:** Week6_Classification.docx, Week7_Classification_Techniques.pdf.

**الكلمات المرمّزة:** القديم 2,744؛ الحالي 6,483؛ المتطابق بالترتيب 112. Old file is labelled Week 11; Weeks 6–7 are not an assured replacement.

1. − OLD [1–111]:
   Regression vs Classification Regression and classification are two main types of supervised machine learning
   tasks but they serve different purposes Regression is used when the goal is to predict a continuous numerical
   value For example predicting the price of a house based on its size location and number of bedrooms is a
   regression problem because the output can take any numeric value Other examples include predicting a person’s
   weight the temperature tomorrow or the stock price for the next day Common regression models include Linear
   Regression Polynomial Regression and Nonlinear Regression In contrast Classification is used when the goal is
   to predict a discrete category or class label For instance predicting
   + 2026 [1–171]:
      Classification in Data Mining 1 Introduction to Classification 1 1 Definition of Classification
      Classification is one of the most important techniques in Data Mining and Machine Learning It is used to
      assign a data record to one of a set of predefined classes Simple Definition Classification is the process
      of learning from previously labeled data and using the learned knowledge to assign a class to new data For
      example a hospital may want to determine whether a patient has a particular disease The possible classes
      could be Disease No Disease The classification model learns from previous patients and then predicts the
      class of a new patient 1 2 Why Classification Is Important Classification is important because many real
      world problems require us to make decisions based on available data For example Healthcare Predict whether
      a patient has a disease Banking Predict whether a customer is likely to default on a loan Education
      Predict whether a student will pass or fail Cybersecurity Determine whether network traffic is normal or
      malicious Email Determine
   + 2026 [180–2003]:
      Business Predict whether a customer will leave a company Therefore classification is widely used for
      prediction and decision making 1 3 Classification as Supervised Learning Classification is a type of
      supervised learning The term supervised means that the training data contains the correct answers For
      example consider a dataset containing patient information Age Glucose BMI Diabetes 25 110 23 5 No 45 180
      31 2 Yes 52 160 29 8 Yes 30 95 22 1 No The first three columns describe the patients The last column
      contains the known class The algorithm studies these examples and learns patterns that can be used to
      classify new patients Basic Idea Labeled Data Classification Algorithm Classification Model New Data
      Predicted Class 1 4 Applications of Classification Classification is used in many areas Medical
      Applications Disease diagnosis Cancer classification Patient risk classification Financial Applications
      Fraud detection Credit risk classification Loan approval Educational Applications Student performance
      prediction Student dropout prediction Pass and fail prediction Cybersecurity Applications Malware
      classification Intrusion detection Phishing detection Business Applications Customer churn prediction
      Customer response prediction Product classification Text Mining Applications Spam detection Sentiment
      classification Document classification Image Applications Object classification Face recognition Medical
      image classification 2 Basic Concepts of Classification Before studying classification algorithms students
      need to understand several important terms 2 1 Dataset A dataset is a collection of data records For
      example a medical dataset may contain information about thousands of patients A student dataset may
      contain information about Student age Attendance Grades Study hours Final result 2 2 Instance An instance
      is one individual record in a dataset For example One patient is one instance One student is one instance
      One email is one instance In a table an instance is usually represented by one row 2 3 Feature A feature
      is an attribute that describes an instance For example patient features may include Age Weight Blood
      pressure Glucose BMI Features are also called Attributes Variables Predictors Features are used by the
      classification model to make predictions 2 4 Class Label The class label is the category that we want to
      predict Examples Diabetes Yes No Cancer Benign Malignant Student Performance Pass Fail Email Spam Not Spam
      The class label is also commonly called the target variable 2 5 Training Data Training data is the data
      used to teach the classification algorithm It contains Features Known class labels The algorithm examines
      the training data and learns patterns 2 6 Validation Data Validation data is used during model development
      It can help us Select between different models Tune model settings Detect overfitting Choose the best
      model Validation data is particularly useful when developing more complex models 2 7 Test Data Test data
      is used to evaluate the final classification model The model should not use the test data during training
      The purpose is to determine how well the model performs on unseen data 3 How Classification Works
      Classification normally involves several stages 3 1 Model Training First we provide the algorithm with
      training data For example Study Hours Attendance Previous Grade Result 2 60 50 Fail 4 75 65 Pass 6 90 80
      Pass 1 50 40 Fail 5 85 75 Pass The algorithm examines the relationship between the features and the class
      It tries to learn patterns that distinguish one class from another 3 2 Model Testing After training the
      model is evaluated using data that it has not seen during training For example Study Hours Attendance
      Previous Grade Actual Result 3 70 55 Fail 6 88 82 Pass The model predicts the results We then compare the
      predictions with the actual results 3 3 Classification of New Data Once we are satisfied with the model's
      performance we can use it to classify new records For example New student Study hours 5 Attendance 88
      percent Previous grade 78 The model may predict Pass The model made this prediction based on patterns
      learned from previous students 3 4 Example of a Classification Problem Consider a hospital that wants to
      classify patients into High Risk Low Risk The hospital has historical patient data Features may include
      Age Blood pressure Cholesterol Weight Previous medical history The model learns from previous patients
      When a new patient arrives the model predicts High Risk or Low Risk 4 Types of Classification There are
      several types of classification problems 4 1 Binary Classification Binary classification contains two
      classes Examples Email Spam Not Spam Medical Diagnosis Disease No Disease Education Pass Fail Banking
      Fraud Not Fraud Binary classification is one of the most common types of classification 4 2 Multiclass
      Classification Multiclass classification contains more than two classes For example an image
      classification system may classify images into Cat Dog Horse Bird Another example is disease
      classification Diabetes Heart Disease Kidney Disease Healthy The model normally assigns one class to each
      instance 4 3 Multilabel Classification In multilabel classification one instance can belong to more than
      one class at the same time For example a research paper could be classified as Artificial Intelligence
      Machine Learning Data Mining The paper can belong to all three categories Difference Multiclass One
      instance One class Multilabel One instance Multiple classes 4 4 Classification and Regression
      Classification and regression are both supervised learning techniques but they predict different types of
      outputs Classification Predicts a category Example Patient Disease or No Disease Regression Predicts a
      numerical value Example Patient Expected blood glucose level Therefore Classification predicts categories
      while regression predicts numerical values 4 5 Classification and Clustering Classification and clustering
      are often confused They are different techniques Classification Clustering Supervised learning
      Unsupervised learning Uses labeled data Uses unlabeled data Classes are already known Groups are
      discovered Used for prediction Used to discover patterns Example If we know that emails are Spam Not Spam
      and we train a model to classify new emails this is classification If we have thousands of emails without
      labels and want to discover groups of similar emails this is clustering 5 Classification Algorithms There
      are many classification algorithms The most important algorithms include Decision Tree Naive Bayes K
      Nearest Neighbors Support Vector Machine Logistic Regression Random Forest Neural Networks 6
      Classification Model Evaluation After building a classification model we need to determine how well it
      performs Model evaluation is important because a model that performs well on training data may not
      necessarily perform well on new data Important evaluation measures include Confusion Matrix Accuracy
      Precision Recall Specificity F1 score ROC Curve AUC 6 1 Confusion Matrix A confusion matrix shows the
      correct and incorrect predictions made by a classification model For binary classification Predicted
      Positive Predicted Negative Actual Positive True Positive False Negative Actual Negative False Positive
      True Negative 6 2 True Positive The actual class is positive The model also predicts positive Example A
      patient has cancer The model predicts cancer This is a True Positive 6 3 True Negative The actual class is
      negative The model also predicts negative Example A patient does not have cancer The model predicts no
      cancer This is a True Negative 6 4 False Positive The actual class is negative The model predicts positive
      Example A patient does not have cancer The model predicts cancer This is a False Positive This can be
      considered a false alarm 6 5 False Negative The actual class is positive The model predicts negative
      Example A patient has cancer The model predicts no cancer This is a False Negative In some medical
      applications false negatives can be particularly serious 6 6 Accuracy Accuracy measures the percentage of
      all predictions that are correct For example Suppose there are 100 patients The model correctly classifies
      95 patients The accuracy is 95 percent Accuracy is easy to understand but it should not always be used
      alone 6 7 Precision Precision answers the question When the model predicts positive how often is it
      correct Formulas For example The model predicts that 100 patients have a disease Only 90 actually have the
      disease The precision is 90 percent Precision is important when false positive predictions are costly 6 8
      Recall Recall answers the question Of all the cases that are actually positive how many did the model
      correctly identify For example There are 100 patients who actually have a disease The model correctly
      identifies 95 of them The recall is 95 percent Recall is especially important when missing a positive case
      can have serious consequences 6 9 Specificity Specificity answers the question Of all the cases that are
      actually negative how many did the model correctly identify For example There are 100 healthy patients The
      model correctly identifies 90 of them as healthy The specificity is 90 percent 6 10 F1 Score F1 score
      combines precision and recall into one measure It is particularly useful when The dataset is imbalanced
      Both false positives and false negatives are important A high F1 score means that the model has a good
      balance between precision and recall 6 11 ROC Curve The ROC curve is used mainly for binary classification
      It evaluates the model at different decision thresholds It considers two important aspects How well the
      model identifies positive cases How often the model incorrectly identifies negative cases as positive A
      model with better separation between the classes generally has a better ROC curve 6 12 AUC AUC means Area
      Under the ROC Curve It provides a single value that summarizes the model's ability to distinguish between
      classes Generally AUC General Interpretation 0 50 Random performance 0 60 0 70 Poor 0 70 0 80 Acceptable 0
      80 0 90 Good 0 90 1 00 Excellent These values should be considered general guidelines rather than strict
      rules 7 Problems in Classification Classification models can face several problems The most important are
      Class imbalance Overfitting Underfitting Irrelevant features Missing data Noisy data 7 1 Class Imbalance
      Class imbalance occurs when one class contains significantly more records than another For example Class
      Number Healthy 9 000 Disease 1 000 The dataset is imbalanced Suppose a model predicts every patient as
      healthy The model would achieve 90 percent accuracy However it would fail to identify any patient with the
      disease Therefore High accuracy does not always mean that a classification model is good 7 2 Overfitting
      Overfitting occurs when the model learns the training data too closely For example Training accuracy 99
      percent Testing accuracy 70 percent The large difference suggests that the model may have learned the
      training data rather than learning general patterns Causes Model is too complex Dataset is too small Too
      many features Noisy data Insufficient regularization 7 3 Underfitting Underfitting occurs when the model
      is too simple to learn the important patterns in the data For example Training accuracy 65 percent Testing
      accuracy 63 percent The model performs poorly on both training and testing data Possible solutions include
      Using a more appropriate algorithm Adding useful features Reducing excessive regularization Improving the
      quality of the data 7 4 Irrelevant Features Not every feature in a dataset is useful For example suppose
      we want to predict
3. − OLD [125–187]:
   or identifying the species of a flower Setosa Versicolor Virginica are classification problems Classification
   models include Logistic Regression Decision Trees Random Forests Support Vector Machines and Neural Networks
   for categorical outputs The key difference is in the type of output regression outputs numbers while
   classification outputs labels In other words regression answers how much while classification answers which
   category Introduction to Regression Regression
   + 2026 [2009–3036]:
      Useful features may include Age Glucose BMI Blood pressure An unrelated feature may add noise without
      helping the prediction Too many irrelevant features can Increase complexity Increase training time Reduce
      model performance Increase the risk of overfitting 7 5 Missing Data Real world datasets often contain
      missing values For example Age Glucose BMI 45 180 31 52 Missing 29 30 95 22 Missing data must be handled
      appropriately before training many classification models Possible approaches include Removing records
      Replacing missing values Using statistical imputation Using model based imputation The appropriate
      approach depends on the dataset and the reason for the missing values 7 6 Noisy Data Noise refers to
      incorrect inconsistent or unnecessary information in the dataset Examples include Incorrect measurements
      Typographical errors Incorrect labels Extreme values caused by measurement errors Data cleaning is an
      important step before classification 8 Improving Classification Performance Several techniques can improve
      classification performance 8 1 Data Preprocessing Data preprocessing prepares the dataset before model
      training It may include Handling missing values Removing duplicates Correcting errors Encoding categorical
      data Scaling numerical features Good preprocessing can significantly affect model performance 8 2 Feature
      Selection Feature selection means choosing the most useful features Suppose a dataset contains 100
      features Only 20 may be strongly related to the target class Using the most useful features can Reduce
      complexity Reduce training time Reduce overfitting Improve interpretability Sometimes improve prediction
      performance Common techniques include Information Gain Chi Square Correlation Mutual Information Recursive
      Feature Elimination Feature Importance 8 3 Feature Scaling Feature scaling ensures that numerical features
      have comparable scales For example Age may range from 18 to 80 Income may range from 1 000 to 100 000 The
      large difference in scale can affect algorithms such as KNN SVM Logistic Regression Neural Networks Common
      scaling methods include Standardization Min Max Scaling Robust Scaling 8 4 Handling Class Imbalance
      Several techniques can be used Oversampling Increase the number of minority class examples Undersampling
      Reduce the number of majority class examples SMOTE SMOTE creates synthetic examples for the minority class
      Class Weights Give greater importance to minority class errors Appropriate Evaluation Measures Use
      Precision Recall F1 score Specificity AUC rather than relying only on accuracy 8 5 Cross Validation Cross
      validation is used to obtain a more reliable estimate of model performance In five fold cross validation
      the dataset is divided into five parts The model is trained and evaluated several times Each part is used
      as the validation set while the remaining parts are used for training The results are then averaged Cross
      validation is especially useful when the available dataset is not very large 8 6 Hyperparameter Tuning
      Classification algorithms contain settings called hyperparameters Examples include KNN Number of neighbors
      Decision Tree Maximum tree depth Random Forest Number of trees SVM Kernel and other model settings
      Hyperparameter tuning attempts to find suitable values for these settings Common methods include Grid
      Search Random Search Bayesian Optimization 8 7 Ensemble Methods An ensemble method combines multiple
      models to produce a stronger prediction Examples include Random Forest Gradient Boosting AdaBoost XGBoost
      The main idea is that combining several models can sometimes produce better and more stable results than
      using one model alone 9 Classification Workflow A complete classification project normally follows a
      sequence of steps Step 1 Data Collection Collect the required dataset Step 2 Data Understanding Study
      Number of records Features Classes Data types Class distribution Step 3 Data Cleaning Handle Missing
      values Duplicate records Incorrect values Noise Step 4 Data Preparation Perform appropriate Encoding
      Scaling Transformation Step 5 Feature Selection Select useful features Step 6 Data Splitting Divide the
      data into appropriate training validation and testing sets Step 7 Model Training Train one or more
      classification algorithms Step 8 Model Evaluation Evaluate the models using appropriate performance
      measures Step 9 Model Tuning Improve the selected model by tuning its hyperparameters Step 10 Final
      Prediction Use the final model to classify new unseen data 10 Comparison of Classification Algorithms
      Algorithm Main Strength Main Weakness Decision Tree Easy to understand Can overfit Naive Bayes Fast and
      simple Strong independence assumption KNN Simple and intuitive Can be slow with large datasets SVM Good
      for complex boundaries Can require careful parameter tuning Logistic Regression Simple and interpretable
      Limited for complex relationships Random Forest Robust and accurate Less interpretable Neural Network
      Powerful for complex data Requires careful training There is no single classification algorithm that is
      best for every dataset The best choice depends on Dataset size Number of features Data type Class
      distribution Complexity of the problem Required interpretability Computational resources 11 Applications
      of Classification Classification has many real world applications 11 1 Healthcare Examples Disease
      diagnosis Cancer classification Patient risk prediction Medical image classification 11 2 Banking and
      Finance Examples Fraud detection Loan approval Credit risk classification Customer risk assessment 11 3
      Education Examples Student performance prediction Dropout prediction Pass and fail prediction Student risk
      classification 11 4 Cybersecurity Examples Intrusion detection Malware classification Phishing detection
      Network traffic classification 11 5 Business Examples Customer churn prediction Customer response
      prediction Product classification Customer risk classification 11 6 Text Mining Examples Spam detection
      Sentiment analysis News classification Document classification 11 7 Image Classification Examples Face
      recognition Object classification Medical image classification Animal classification 12 Practical
      Classification Example Breast Cancer Classification Consider a breast cancer dataset The dataset contains
      information about breast tumors Features Examples include Tumor size Cell characteristics Texture Shape
      Other medical measurements Classes The target class may be Benign Malignant Practical Process Step 1 Load
      the dataset Step 2 Examine the features and classes Step 3 Check for missing values Step 4 Check whether
      the classes are balanced Step 5 Prepare the features Step 6 Divide the data into training and testing sets
      Step 7 Train several classification algorithms Logistic Regression Decision Tree KNN SVM Random Forest
      Step 8 Evaluate each model Use Accuracy Precision Recall Specificity F1 score AUC Step 9 Compare the
      results Step 10 Select the most appropriate model The best model should not necessarily be the model with
      the highest accuracy For a medical application recall and specificity may be particularly important
      LECTURE RULE BASED CLASSIFIERS Course Data Mining Topic Classification Techniques Level Master's Students
      1 Introduction Classification
4. − OLD [193–360]:
   used to predict continuous numerical values based on input data Unlike classification which assigns labels
   regression estimates real valued outputs such as prices temperature or medical measurements Example
   Predicting house prices based on size location and number of rooms Predicting a patient’s blood sugar level
   based on age BMI and blood pressure Predicting stock prices or sales revenue Goal The goal of regression is
   to find a relationship function between input features and a continuous target variable Mathematically Where
   the regression model the random error term unexplained variation Why Regression Matters Regression helps in
   Forecasting e g sales prediction demand estimation Trend analysis e g population growth disease spread Risk
   assessment e g predicting loan default Scientific modeling e g dose response analysis in healthcare In
   machine learning regression is foundational for Understanding relationships between variables Building
   predictive models for continuous outcomes Serving as the basis for more advanced models e g neural networks
   Types of Regression 1 Linear Regression The simplest and most widely used regression method
   + 2026 [3042–6318]:
      in data mining used to assign data objects to predefined classes A model learns from labeled training data
      and uses that knowledge to predict the class of new data A rule based classifier uses a collection of IF
      THEN rules to assign class labels Example IF attendance is high AND the exam mark is at least 50 THEN the
      student passes 2 Definition and Structure A rule based classifier represents classification knowledge in
      the form IF condition THEN class Antecedent the IF part containing the conditions that must be satisfied
      Consequent the THEN part containing the predicted class Example IF Age 30 AND Income High THEN Loan Status
      Approved Here Age 30 AND Income High is the antecedent and Loan Status Approved is the consequent 3
      Conditions and Logical Operators A rule can contain one or more conditions connected by logical operators
      such as AND and OR Example IF Attendance 75 AND Exam Mark 50 THEN Result Pass The AND operator means both
      conditions must be true for the rule to apply An OR operator means at least one of its connected
      conditions must be true 4 How Rule Based Classification Works 1 Prepare the dataset by collecting and
      cleaning the data 2 Generate IF THEN rules from the training data 3 Evaluate how accurately the rules
      classify training examples 4 Apply the rules to a new data record 5 Assign the predicted class based on
      the matching rule or rules Example dataset Student Attendance Exam mark Result S1 90 80 Pass S2 85 65 Pass
      S3 60 45 Fail S4 50 35 Fail S5 80 40 Fail Possible rules Rule 1 IF Exam Mark 50 THEN Result Pass Rule 2 IF
      Exam Mark 50 THEN Result Fail Student S1 has a mark of 80 so Rule 1 predicts Pass Student S3 has a mark of
      45 so Rule 2 predicts Fail 5 Types of Rule Based Classifiers 5 1 Ordered Rules Rules are evaluated in a
      specific sequence The first matching rule determines the predicted class Therefore rule order can affect
      the result when multiple rules match 5 2 Unordered Rules Rules do not necessarily have a fixed priority If
      multiple rules match the classifier may use voting rule quality or another conflict resolution strategy 5
      3 Default Rule A default rule handles a record when no explicit rule matches Rule 1 IF Exam Mark 50 THEN
      Result Pass Rule 2 IF Exam Mark 40 THEN Result Fail Default Result Fail A mark of 45 matches neither
      explicit rule so the default rule assigns Fail 6 Rule Coverage and Rule Accuracy 6 1 Rule Coverage
      Coverage is the proportion of records that satisfy a rule's conditions Coverage R Number of records
      satisfying R Total number of records Example If 40 of 100 students satisfy a rule coverage 40 100 0 40 or
      40 6 2 Rule Accuracy Rule accuracy is the proportion of records covered by a rule that belong to the class
      predicted by that rule Accuracy R Correctly classified covered records All records covered by R Example If
      a rule covers 40 students and correctly classifies 36 accuracy 36 40 0 90 or 90 Coverage measures how many
      records a rule applies to Accuracy measures how often the rule predicts the correct class among those
      records 7 Conflict Resolution A conflict occurs when two or more rules match the same record but predict
      different classes Rule 1 IF Attendance 75 THEN Result Pass Rule 2 IF Exam Mark 50 THEN Result Fail A
      student with 80 attendance and a mark of 40 matches both rules which predict different classes Common
      conflict resolution approaches include Rule priority prefer the rule with higher priority Rule ordering
      use the first matching rule Rule quality select the rule with stronger performance on training data Voting
      matching rules vote for a class Default class use a predefined class when needed 8 How Classification
      Rules Are Generated 8 1 Direct Rule Generation Some algorithms learn rules directly from training data by
      identifying conditions that frequently correspond to particular classes 8 2 Extracting Rules from Decision
      Trees A decision tree can be converted into IF THEN rules Each path from the root to a leaf becomes a rule
      IF Exam Mark 50 THEN Result Pass IF Exam Mark 50 THEN Result Fail 8 3 Sequential Covering Sequential
      covering generates rules one at a time 6 Find a rule that correctly classifies a group of training records
      7 Add the rule to the rule set 8 Remove or set aside covered records depending on the algorithm 9 Repeat
      to learn additional rules 10 Stop when a suitable stopping condition is reached RIPPER is an example of a
      rule learning algorithm that uses a sequential covering approach 9 Common Algorithms Algorithm Main idea
      OneR Builds a simple classifier using one attribute RIPPER Learns rules using sequential covering and
      simplifies them CN2 Learns classification rules using heuristic search PART Generates rules from partial
      decision trees 10 Advantages Interpretability rules are usually easy to understand Transparency a
      prediction can be explained by showing the matching rule Flexibility rules can combine multiple attributes
      Knowledge representation rules express knowledge in a human readable form Practical implementation simple
      rules can be implemented with conditional statements 11 Limitations Conflicting rules may predict
      different classes Complex datasets may require a large number of rules Overfitting can occur when rules
      describe training examples too specifically Some records may not match any explicit rule Large rule sets
      can be difficult to maintain Rule pruning rule ordering default classes and validation on unseen data can
      help address these limitations 12 Rule Based Classifiers vs Decision Trees Feature Rule Based Classifier
      Decision Tree Representation IF THEN rules Tree structure Prediction Evaluate applicable rules Follow a
      path from root to leaf Interpretability Often clear for small rule sets Often clear for small trees
      Overlapping conditions Possible One path is followed in a standard tree Generation Learned directly or
      extracted Built by recursively splitting data Complexity May contain overlapping rules May contain many
      branches and leaves A decision tree can be converted into rules but a rule based classifier does not have
      to originate from a decision tree 13 Practical Example Loan Approval Suppose a bank classifies loan
      applications as Approved or Rejected using income and credit history Rule 1 IF Credit History Good AND
      Income High THEN Loan Status Approved Rule 2 IF Credit History Poor THEN Loan Status Rejected Rule 3 IF
      Income Low THEN Loan Status Rejected Default rule Loan Status Rejected An applicant with good credit
      history and high income satisfies Rule 1 and is predicted as Approved An applicant with poor credit
      history matches Rule 2 and is predicted as Rejected In real lending systems rules must be validated and
      comply with applicable regulations 14 Summary A rule based classifier is a supervised classification
      technique that uses IF THEN rules to assign class labels Each rule contains an antecedent conditions and a
      consequent predicted class Key concepts include rule generation and application ordered and unordered
      rules coverage and accuracy conflict resolution default classes and the advantages and limitations of rule
      based classification Rule based classifiers are particularly useful when understanding why a prediction
      was made is as important as obtaining the prediction itself Important distinction During training the
      output labels guide the creation and selection of rules During prediction the output is unknown so the
      classifier applies the learned rules to the input attributes to predict the class NAIVE BAYES ALGORITHM 1
      Introduction Naive Bayes is a supervised machine learning algorithm used for classification It predicts
      the class of a new record by calculating the probability that the record belongs to each possible class It
      is based on Bayes theorem and assumes that input attributes are conditionally independent given the class
      Applications include email spam detection sentiment analysis medical diagnosis document classification and
      weather prediction 2 Bayes Theorem Bayes theorem calculates the probability of a class given observed
      evidence P C X P X C x P C P X Where P C X Posterior probability probability of class C given attributes X
      P X C Likelihood probability of observing X when the class is C P C Prior probability probability of class
      C before considering the attributes P X Evidence overall probability of observing X Observed attributes
      update our estimate of which class is most likely 3 Why Is It Called Naive Bayes It is called naive
      because it assumes input attributes are conditionally independent when the class is known For example a
      student classifier might use attendance study hours and assignment completion to predict Pass or Fail
      Naive Bayes assumes these attributes are conditionally independent given the result Real attributes may be
      related but the algorithm can still perform well 4 How Naive Bayes Works The algorithm generally follows
      these steps 11 Collect labeled training data 12 Calculate the prior probability of each class 13 Calculate
      the likelihood of each attribute value for each class 14 Calculate a score or posterior probability for
      each candidate class 15 Predict the class with the highest score Predicted class argmax over C of P C x P
      X C Under the conditional independence assumption the likelihood is calculated as a product P X C P x1 C x
      P x2 C x x P xn C The evidence P X is the same for each candidate class so it can be omitted when
      comparing class scores 5 Worked Example Weather Prediction Suppose we predict whether people will play
      outside based on Weather and Temperature Weather Temperature Play Sunny Mild Yes Sunny Hot No Rainy Mild
      Yes Rainy Cold No Sunny Mild Yes Rainy Mild No Sunny Mild Yes Rainy Cold No New record Weather Sunny
      Temperature Mild Predict Play Step 1 Calculate prior probabilities There are 8 records 4 have Play Yes and
      4 have Play No P Yes 4 8 0 5 P No 4 8 0 5 Step 2 Calculate likelihoods Among the four Yes records three
      are Sunny and all four have Mild temperature P Sunny Yes 3 4 0 75 P Mild Yes 4 4 1 Among the four No
      records one is Sunny and one has Mild temperature P Sunny No 1 4 0 25 P Mild No 1 4 0 25 Step 3 Calculate
      class scores For Play Yes Score Yes 0 5 x 0 75 x 1 0 375 For Play No Score No 0 5 x 0 25 x 0 25 0 03125
      Step 4 Choose the highest score The Yes score 0 375 is greater than the No score 0 03125 so the prediction
      is Play Yes After normalization the probabilities are approximately 92 3 for Yes and 7 7 for No The
      unnormalized scores are sufficient for comparing classes 6 Zero Probability and Laplace Smoothing If an
      attribute value never occurs in a class its estimated likelihood is zero Multiplying by zero can make the
      entire score for that class zero Laplace smoothing adds a small count to each possible value For a
      categorical attribute P xi C N xi C alpha N C alpha x K N xi C is the number of records in class C with
      value xi N C is the total records in class C K is the number of possible attribute values alpha is the
      smoothing parameter commonly 1 7 Types of Naive Bayes Type Suitable data Example Gaussian Naive Bayes
      Continuous numeric attributes Height weight laboratory measurements Multinomial Naive Bayes Count data
      Word counts in documents Bernoulli Naive Bayes Binary attributes Whether a word occurs or does not occur
      Gaussian Naive Bayes assumes numeric attributes follow a Gaussian distribution within each class
      Multinomial Naive Bayes is often used for word frequency counts Bernoulli Naive Bayes is useful for binary
      features 8 Advantages Simple and computationally efficient Works well for many high dimensional datasets
      Requires relatively little training data for some problems Supports multiple classes Provides class
      probability estimates 9 Limitations The conditional independence assumption may not hold Zero
      probabilities can cause problems without smoothing Probability estimates may be poorly calibrated
      Performance may be weaker when attributes are strongly dependent 10 Naive Bayes vs Rule Based Classifiers
      Feature Naive Bayes Rule Based Classifier Main approach Probability calculations IF THEN rules Training
      Estimates prior and likelihood probabilities Learns or receives classification rules Prediction Chooses
      the most probable class Applies matching rules Assumptions Commonly assumes conditional independence
      Depends on rule learning method Interpretability Uses class probabilities Individual rules are often easy
      to explain 11 Student Exercises 16 A dataset contains 100 records 60 belong to Class A and 40 to Class B
      Calculate both prior probabilities 17 In Class A 30 out of 60 records have Weather Sunny Calculate P Sunny
      A 18 If P A 0 6 P Sunny A 0 5 and P Mild A 0 8 calculate the Naive Bayes score for Class A 19 Explain why
      Naive Bayes is called naive 20 Explain the purpose of Laplace smoothing Exercise Answers 21 P A 60 100 0 6
      P B 40 100 0 4 22 P Sunny A 30 60 0 5 23 Score A 0 6 x 0 5 x 0 8 0 24 24 It assumes attributes are
      conditionally independent given the class 25 It prevents zero likelihood estimates by adding a small count
      to possible attribute values 12 Summary Naive Bayes is a probabilistic classification algorithm based on
      Bayes theorem It uses prior probabilities and likelihoods to estimate the most probable class Essential
      concepts include prior probability likelihood posterior probability conditional independence Laplace
      smoothing and selecting the class with the highest score The key difference from a rule based classifier
      is that Naive Bayes calculates class probabilities whereas a rule based classifier uses IF THEN conditions
      Logistic Regression Algorithm A Lecture for Machine Learning and Data Mining Students Learning Objectives
      Define Logistic Regression and explain its main purpose Understand the sigmoid function and how it
      converts a linear score into a probability Follow the main steps used to train and apply a Logistic
      Regression model Calculate predicted probabilities and convert them into class labels using a decision
      threshold Understand common evaluation metrics advantages and limitations 1 Introduction Logistic
      Regression is a supervised machine learning algorithm used mainly for classification It estimates the
      probability that an observation belongs to a particular class Although its name contains the word
      regression it is commonly used for classification tasks Examples include predicting whether a student will
      pass or fail whether a customer will leave a service whether an email is spam or whether a medical test
      result is positive or negative 2 Types of Logistic Regression Binary Logistic Regression predicts one of
      two classes such as Yes or No Multinomial Logistic Regression predicts one of three or more unordered
      classes Ordinal Logistic Regression models categories that have a meaningful order such as Low Medium and
      High Specific ordinal models use assumptions that differ from ordinary binary Logistic Regression 3 How
      Logistic Regression Works Logistic Regression first calculates a linear score from the input features It
      then applies the sigmoid function to convert that score into a value between 0 and 1 interpreted as a
      probability The linear score is z b b x b x b x where x x x are input features b is the intercept bias b b
      b are learned model coefficients z is the linear score 4 The Sigmoid Function The sigmoid function is P Y
      1 X 1 1 e The sigmoid function maps any real valued score z to a value strictly between 0 and 1 This
      output can be interpreted as the estimated probability of the positive class For example If z 0 then P Y 1
      X 1 1 e 0 5 If z 2 then P Y 1 X 1 1 0 1353 0 8808 If z 2 then P Y 1 X 1 1 7 389 0 1192 5 Decision
      Threshold and Class Prediction For binary classification a threshold converts the estimated probability
      into a class label A common default is 0 5 although the threshold can be adjusted for the task If P Y 1 X
      0 5 predict Class 1 If P Y 1 X 0 5 predict Class 0 Example if the predicted probability is 0 78 and the
      threshold is 0 5 the predicted class is 1 This does not mean the model is 78 accurate it means the model
      estimates a 78 probability for Class 1 6 Worked Numerical Example Suppose we want to predict whether a
      student passes an exam Pass 1 Fail 0 based on the number of hours studied For illustration assume a
      trained Logistic Regression model has the following equation z 4 1 2x where x is the number of hours
      studied The intercept and coefficient are assumed to have been learned during training Example A A student
      studies for 4 hours Step 1 Calculate the linear score z 4 1 2 4 0 8 Step 2 Apply the sigmoid function P
      Pass 1 x 4 1 1 e 1 1 0 4493 0 6900 Step 3 Apply the threshold of 0 5 Because 0 6900 0 5 predict Pass Class
      1 Example B A student studies for 2 hours z 4 1 2 2 1 6 P Pass 1 x 2 1 1 e 0 1680 Because 0 1680 0 5
      predict Fail Class 0 These calculations demonstrate prediction after training In a real application the
      coefficients are estimated from labeled training data 7 Main Training Steps 26 Prepare data Collect
      labeled examples and identify the input features and target class 27 Preprocess features Handle missing
      values and encode categorical inputs when necessary Scaling numeric features can help optimization
      especially when feature magnitudes differ 28 Split the data Separate training data from validation or test
      data to evaluate generalization 29 Initialize the model Set up the Logistic Regression model and its
      training objective 30 Learn coefficients Estimate the intercept and feature coefficients by optimizing the
      logistic loss commonly binary cross entropy often with regularization 31 Estimate probabilities For each
      new record calculate z and apply the sigmoid function 32 Assign a class Compare the probability with a
      chosen decision threshold 33 Evaluate Assess predictions on held out data using appropriate metrics 8 How
      Are the Coefficients Learned The coefficients are not normally chosen by hand The training algorithm
      adjusts them to make the predicted probabilities fit the observed labels For binary classification a
      common objective is binary cross entropy log loss L 1 N y log p 1 y log 1 p Here N is the number of
      training examples y is the actual label 0 or 1 and p is the predicted probability for Class 1 Optimization
      methods such as gradient based methods or solver specific methods minimize this loss Regularization may be
      added to reduce overfitting 9 Interpreting Coefficients A coefficient describes the change in the log odds
      of the positive class associated with a one unit increase in that feature holding the other features
      constant The odds ratio for a one unit increase is exp b For example if b 0 7 then exp 0 7 2 01 Under the
      model a one unit increase in that feature multiplies the odds of Class 1 by about 2 01 holding other
      features constant This is an odds interpretation not a direct doubling of probability 11 Advantages Simple
      to implement and relatively fast to train Produces probabilities that can support threshold based
      decisions Coefficients can be interpreted through log odds and odds ratios Provides a strong baseline for
      many binary classification problems Can use regularization to help control overfitting 12 Limitations The
      basic model
5. − OLD [367–2744]:
   variables and the target Equation Where intercept coefficients weights for each feature Assumptions of Linear
   Regression Linear Regression works correctly only when certain assumptions are satisfied The main assumptions
   are 1 Linearity The relationship between independent variables X and dependent variable y must be linear
   Means the effect of X on y is constant 2 Independence of Errors The residuals errors must be independent of
   each other No correlation between errors Especially important for time series data 3 Homoscedasticity
   Constant Variance The residuals should have constant variance across all levels of X If variance changes e g
   increasing or decreasing it is called heteroscedasticity violates this assumption 4 Normality of Errors The
   residuals should be normally distributed Important for hypothesis testing and confidence intervals 5 No
   Multicollinearity for multiple regression Independent variables should not be highly correlated with each
   other High multicollinearity causes unstable coefficients 6 No Autocorrelation Residuals should not be
   correlated with themselves common in time series Checked using the Durbin Watson test 7 X variables are
   measured without error Predictors should be fairly accurate and reliable Example Predicting House Prices
   Using Linear Regression In this example we aim to predict the price of a house based on its size measured in
   square feet The underlying assumption is that larger houses generally cost more and this relationship can be
   represented as a straight line hence the use of linear regression 1 The Dataset We are given the following
   data House Size sqft Price 1000s 1000 200 1500 250 2000 280 2500 310 3000 360 Each row represents one house
   showing how the price tends to increase as the size increases 2 The Linear Regression Model Linear regression
   assumes that the relationship between the independent variable house size and the dependent variable house
   price can be expressed with a straight line Where is the predicted house price is the house size is the
   intercept representing the price when the size is zero a theoretical starting point and is the slope
   indicating how much the price increases for every additional square foot 3 Determining the Best Fit Line The
   goal of linear regression is to find the values of and that make the model’s predictions as close as possible
   to the actual prices in the dataset It does this by minimizing the total squared difference between the
   actual and predicted prices a process called least squares estimation 4 Interpreting the Model After training
   the model on this data we might obtain an equation like This means The intercept 110 suggests that even a
   very small house has a base cost of about 110 000 The slope 0 083 means that for each additional square foot
   the house price increases by approximately 83 5 Making Predictions Using the model we can estimate the price
   of a new house For example if a house is 2200 sqft we substitute it into the equation So the model predicts
   that a 2200 square foot house would cost approximately 292 600 2 Multiple Linear Regression Involves two or
   more independent variables Example Example Multiple Linear Regression Predicting House Prices Using Several
   Features 1 Problem Statement In the earlier example we used only one feature house size to predict the price
   of a house However in the real world house prices depend on several factors not just size To make our
   predictions more accurate we now include multiple input variables such as House size in square feet Number of
   bedrooms Distance to city center in km This type of model is called Multiple Linear Regression because it
   uses more than one predictor variable 2 The Dataset House Size sqft Bedrooms Distance to City Center km Price
   1000s 1000 2 10 200 1500 3 8 250 2000 3 5 300 2500 4 4 350 3000 4 2 400 This data shows that larger houses
   with more bedrooms and closer to the city center tend to cost more 3 The Multiple Linear Regression Model The
   relationship between inputs and output can be expressed as Where Predicted house price Intercept base price
   when all features are zero House size Number of bedrooms Distance to city center Coefficients showing how
   much each feature affects the price 4 Interpreting the Model Suppose after training the model we obtain the
   following equation Here’s what each coefficient means Intercept 80 The base price is 80 000 when all other
   features are 0 theoretical starting point Size coefficient 0 07 Every additional square foot adds 70 to the
   price Bedrooms coefficient 15 Each additional bedroom increases the price by 15 000 Distance coefficient 10
   For every extra kilometer away from the city center the price decreases by 10 000 5 Making Predictions Let’s
   predict the price for a new house with Size 2200 sqft Bedrooms 3 Distance 5 km Substitute the values into the
   equation So the model predicts that this house would cost approximately 229 000 3 Polynomial Regression
   Captures nonlinear relationships by adding powers of features Example Polynomial Regression Polynomial
   Regression is a type of regression analysis where the relationship between the independent variable X and the
   dependent variable Y is not linear but instead follows a curved non linear pattern 1 Problem Statement Let’s
   say we are studying the relationship between years of experience and salary for employees in a company We
   collect the following data Years of Experience X Salary 1000s Y 1 40 2 45 3 55 4 70 5 90 6 120 7 150 8 190 If
   we plot this data we see that salary doesn’t increase in a straight line Instead it increases slowly at first
   then faster as experience grows suggesting a curved trend This means a simple linear regression straight line
   won’t fit the data well 2 Polynomial Regression Model To capture the curved relationship we use a polynomial
   equation such as Here is the predicted salary is the years of experience is the squared term that captures
   the curve are coefficients estimated by the model 3 Example Equation After fitting the polynomial regression
   to our data we might get Interpreting this equation Intercept 35 Base salary when experience is 0 years
   Linear term 4x For each extra year of experience salary increases by roughly 4 000 initially Quadratic term 1
   5x As experience grows this squared term accelerates salary growth reflecting the non linear trend 4 Making
   Predictions Let’s predict the salary for an employee with 5 years of experience Predicted salary 92 500 You
   can see how this matches the actual trend from the data table above salaries increase faster as experience
   grows 4 Logistic Regression Despite its name logistic regression is a classification algorithm It predicts
   probabilities between 0 and 1 using the sigmoid function Example Predicting Whether a Patient Has Diabetes
   Problem Statement We want to predict if a patient has diabetes Yes 1 No 0 based on several features Age in
   years BMI Body Mass Index Blood Pressure mmHg Glucose Level mg dL Since the outcome is binary Logistic
   Regression is appropriate Sample Data Conceptual Age BMI Blood Pressure Glucose Diabetes 25 22 5 120 85 0 40
   30 0 140 160 1 35 28 0 130 140 1 50 26 0 125 100 0 Logistic Regression Formula Multiple Features Where
   intercept baseline log odds when all features 0 coefficients showing how each feature affects the probability
   of diabetes Interpretation Each coefficient tells us how much the log odds of having diabetes change when
   that feature increases by 1 unit holding other features constant Example for BMI each additional BMI unit
   slightly increases the chance of diabetes for Glucose each additional glucose unit increases the chance of
   diabetes After calculating the sum of we convert it to a probability using the sigmoid function Example
   Prediction Suppose the model gives coefficients For a patient Age 45 BMI 28 BP 130 Glucose 150 the log odds
   would be Probability of diabetes Interpretation The patient has a very high probability of having diabetes 5
   Decision Tree and Random Forest Regression Decision Tree Regression splits data into smaller regions and
   predicts based on averages Random Forest Regression combines multiple trees for more robust predictions These
   are non parametric models that work well on complex data 6 Support Vector Regression SVR Based on Support
   Vector Machines Tries to fit the best line within a margin of tolerance epsilon Robust to outliers and
   effective for high dimensional data Steps in Regression Modeling Data Collection Gather input and target data
   Data Preprocessing Handle missing values Normalize or scale features Encode categorical variables Splitting
   Data Divide into training and test sets e g 80 train 20 test Model Training Fit the regression model on
   training data Prediction Use the trained model to predict on new data Evaluation Measure model performance
   using evaluation metrics Regression Evaluation Metrics Metric Formula Interpretation Mean Absolute Error MAE
   frac 1 n sum y i hat y i Mean Squared Error MSE Penalizes larger errors Root Mean Squared Error RMSE Same
   scale as target variable R Score Coefficient of Determination Measures model fit 1 perfect 1 Mean Absolute
   Error MAE Mean Absolute Error MAE is a metric used to measure how far predictions are from the actual values
   It calculates the average of the absolute differences between predicted values and actual values Formula
   Where actual value predicted value number of observations absolute error Meaning MAE tells you on average how
   much the predictions are wrong Lower MAE better model Example If MAE 3 the model’s predictions are off by 3
   units on average Characteristics of MAE Uses absolute errors no direction considered Easy to understand Less
   sensitive to outliers than MSE or RMSE Works well when errors are evenly distributed Example Actual values 10
   15 Predicted values 8 14 Errors 10 8 2 15 14 1 So the model’s average error 1 5 units Mean Absolute Error MAE
   is the average of the absolute differences between actual and predicted values It measures how much
   predictions deviate from the true values on average A lower MAE means a more accurate model 2 Mean Squared
   Error MSE Mean Squared Error MSE is a popular error metric used to measure how far predictions are from
   actual values It calculates the average of the squared differences between predicted and actual values
   Formula Where actual value predicted value number of observations squared error MSE tells you how large the
   prediction errors are but it penalizes large errors more heavily because of the squaring Lower MSE better
   model Characteristics of MSE Penalizes large errors strongly More sensitive to outliers than MAE Commonly
   used in regression and optimization Smooth and differentiable useful for gradient based learning e g neural
   networks Example Actual values 10 15 Predicted values 8 14 Errors So the average squared error 2 5 Mean
   Squared Error MSE is the average of the squared differences between actual and predicted values It penalizes
   large errors more because of squaring A smaller MSE indicates a more accurate model 3 Root Mean Squared Error
   RMSE Root Mean Squared Error RMSE is a metric used to measure how far predictions are from actual values It
   is the square root of the Mean Squared Error MSE It shows the average error in the same units as the original
   data Formula Where actual value predicted value number of data points squared error Meaning RMSE tells you
   How large prediction errors are on average In the same units as the target variable With stronger penalty for
   large errors because of the squaring inside Lower RMSE better model Characteristics of RMSE Penalizes large
   errors more like MSE Easy to interpret because It is in the same units as the data Sensitive to outliers
   Commonly used in regression and forecasting Example Actual values 10 15 Predicted values 8 14 Squared errors
   4 and 1 So the model’s average error 1 58 units Root Mean Squared Error RMSE is the square root of the
   average squared differences between actual and predicted values It penalizes large errors more strongly but
   expresses the error in the same units as the actual data A lower RMSE indicates better prediction performance
   4 R Score Coefficient of Determination R R squared is a metric that shows how well a regression model
   explains the variability of the target Y It tells you how much of the variation in the dependent variable is
   explained by the model Formula Where sum of squared residuals total sum of squares Meaning R 1 Perfect model
   explains 100 of the variance R 0 Model explains none of the variance R 0 Model is worse than simply
   predicting the mean Higher R Better model Interpretation Very Simple If R 0 85 it means The model explains 85
   of the variation in the output variable Only 15 is left unexplained Characteristics of R Works for regression
   only not classification Measures the goodness of fit Easy to interpret Can be misleading if Too many
   variables overfitting Model is nonlinear Data contains noise Example Actual values 10 12 14 Predicted 11 13
   15 Compute Mean So the model explains 62 5 of the variance R Coefficient of Determination measures how much
   of the variation in the dependent variable is explained by the regression model It ranges from negative
   values to 1 where 1 means a perfect fit and 0 means the model explains none of the variance Higher R
   indicates a better model Main Differences MSE vs MAE vs RMSE Metric Uses Absolute or Squared Error Sensitive
   to Outliers Units Penalty on Large Errors MAE Absolute No Same as data Low MSE Squared Yes Squared units High
   RMSE Squared then root Yes Same as data High When to Use Which Use MAE when Data has outliers You want a
   simple robust metric You want equal weight for all errors Use MSE when You want large errors to be punished
   severely You care about outliers Training neural networks or models using gradient descent Use RMSE when You
   want the benefits of MSE But want results in original units And you want easier interpretation MAE averages
   the absolute errors and is robust to outliers MSE averages the squared errors and penalizes large mistakes
   more strongly RMSE is the square root of MSE giving a more interpretable error in the same units as the
   target Lower values of all metrics indicate better model performance
   + 2026 [6325–6483]:
      features and the log odds of the outcome It may not capture complex nonlinear patterns unless features are
      transformed or interactions are added Performance can be affected by outliers multicollinearity poor
      feature design or data quality A probability estimate is not automatically well calibrated calibration
      should be checked when important The default 0 5 threshold may not be suitable when false positives and
      false negatives have different costs 13 Logistic Regression vs Naive Bayes Aspect Logistic Regression
      Naive Bayes Model type Discriminative models P Y X Generative models P X Y and P Y Main approach Learns
      coefficients by optimizing a loss function Estimates priors and likelihoods from training data Feature
      assumption No conditional independence assumption is required Uses a conditional independence assumption
      in its standard form Output Class probabilities and labels Class probabilities and labels Useful when A
      flexible linear decision boundary and interpretable coefficients are useful Training data are limited or
      conditional feature distributions are reasonably modeled

## Data classification diagnostic comparison

**المصادر القديمة:** DM_Data_Classification (archive).docx.  **مصادر 2026:** Week4_Feature_Selection.docx, Week6_Classification.docx, Week7_Classification_Techniques.pdf.

**الكلمات المرمّزة:** القديم 4,810؛ الحالي 8,459؛ المتطابق بالترتيب 475. Old file mixes security classification with feature selection and ML classification; diagnostic only.

1. − OLD [1–56]:
   Definition of Data Classification Data classification is the process of organizing information into
   categories based on its sensitivity and potential impact if compromised In cybersecurity for businesses data
   classification helps identify and prioritize sensitive information needing strong protection By categorizing
   data companies can apply appropriate security measures to safeguard critical information Feature Selection
   for Classification Overview
   + 2026 [1–6]:
      Feature Selection Techniques in Data Mining
2. − OLD [63–63]:
   choosing
   + 2026 [13–13]:
      selecting
3. − OLD [72–532]:
   that contribute the most to predicting the target class It helps reduce noise improve model accuracy and make
   models faster and easier to interpret 2 1 Why Feature Selection is Important Benefit Description Improves
   Model Accuracy Removes irrelevant or redundant data that can confuse the model Reduces Training Time Fewer
   features less computation Prevents Overfitting Less chance for the model to memorize noise Improves
   Interpretability Models become simpler and easier to explain Types of Features Type Description Example
   Relevant Useful and contribute to class prediction Age blood sugar in diabetes prediction Irrelevant
   Unrelated to target ID number random noise Redundant Duplicates information of other features Height in
   inches height in cm 2 2 Feature Selection vs Feature Extraction Aspect Feature Selection Feature Extraction
   Purpose Selects a subset of original features Creates new features by transforming data Example Selecting top
   10 features using Chi square PCA Principal Component Analysis Output Subset of existing features Set of new
   transformed features 2 3 Steps in Feature Selection for Classification 1 Remove constant and duplicate
   features 2 Handle missing values and normalize data 3 Compute feature importance Filter Wrapper Embedded 4
   Select top k important features 5 Evaluate classification performance 6 Optionally perform cross validation
   to verify stability Common Challenges Issue Description Curse of Dimensionality Too many irrelevant features
   can reduce accuracy Feature Interactions Some features are only useful in combination Overfitting on Small
   Data Too aggressive selection may remove informative attributes Feature Selection Techniques by Data Type
   Data Type Recommended Methods Categorical Chi square Mutual Information Cramer’s V Numeric Correlation ANOVA
   ReliefF Mixed Categorical Numeric Mutual Information Random Forest Importance K Prototypes clustering based
   methods Example Feature Selection in Practice Imagine you’re building a classifier to detect spam emails Step
   Technique Result Step 1 Remove low variance words Drop words appearing in 1 of emails Step 2 Apply Chi square
   test Keep only words highly correlated with spam ham Step 3 Use model based selection Train Logistic
   Regression with L1 LASSO regularization to keep most predictive words Summary Table Method Type Examples Pros
   Cons Filter Chi square Info Gain Fast independent of model May ignore feature interactions Wrapper RFE
   Forward Backward Considers interactions Slow computationally expensive Embedded LASSO Tree Importance Balance
   of speed and accuracy Depends on chosen algorithm In Short Feature Selection chooses the most informative and
   relevant features for building accurate efficient and interpretable classifiers It’s essential for handling
   high dimensional datasets and avoiding overfitting Methods of Feature Selection There are three main
   approaches Filter Methods Use statistical tests to score each feature independently of the classifier Simple
   and fast Do not depend on the learning algorithm Examples Method Description Common Use Chi Square Test
   Measures dependency between feature and target for categorical data Text classification categorical data
   Information Gain Mutual Information
   + 2026 [22–787]:
      while removing irrelevant or redundant features For example if we want to predict whether a patient has
      diabetes the dataset may contain Age Glucose BMI Blood Pressure Insulin Skin Thickness Pregnancies Patient
      ID Some features may contribute strongly to prediction while others may provide little or no useful
      information Feature selection attempts to keep the useful features and remove the unnecessary ones Why is
      Feature Selection Important Feature selection can Reduce the number of features Remove irrelevant and
      redundant features Reduce computational cost Improve model performance in some cases Reduce the risk of
      overfitting Make the model easier to interpret Help visualize high dimensional data Main Feature Selection
      Techniques Feature selection techniques are commonly divided into three main categories Filter Methods
      Wrapper Methods Embedded Methods A simple way to remember them is Filter evaluate features Wrapper
      evaluate feature subsets using a model Embedded select features during model training 1 Filter Methods
      Filter methods select features based on their statistical characteristics without using a data mining
      algorithm to evaluate the final feature subset They are usually fast and suitable for datasets with many
      features Common Filter Techniques 1 1 Correlation Correlation measures the relationship between two
      variables For example Feature Correlation with Target Glucose 0 47 BMI 0 29 Age 0 24 Patient ID 0 01
      Features with very weak relationships with the target may be removed Example If the correlation between
      Patient ID and diabetes is approximately 0 Patient ID is probably not useful for prediction Important Low
      correlation does not always mean that a feature is useless because correlation mainly captures certain
      types of relationships especially linear relationships How to Calculate Correlation In data mining
      correlation measures the strength and direction of the relationship between two numerical variables The
      most commonly used measure is Pearson correlation coefficient denoted by 1 Pearson Correlation Formula
      Where value of variable value of variable mean of mean of number of observations correlation coefficient 2
      Simple Example Suppose we have Age and Blood Pressure for five people Person Age X Blood Pressure Y 1 20
      110 2 30 120 3 40 130 4 50 140 5 60 150 Step 1 Calculate the means Step 2 Calculate deviations X Y 20 110
      20 20 30 120 10 10 40 130 0 0 50 140 10 10 60 150 20 20 Step 3 Calculate the products Therefore Step 4
      Calculate squared deviations Similarly Step 5 Calculate So the correlation is This means there is a
      perfect positive linear correlation between Age and Blood Pressure in this example 1 2 Chi Square Test The
      Chi square test measures the relationship between categorical features and a categorical target For
      example Smoking Status Heart Disease A high Chi square statistic indicates a stronger association between
      the feature and the target It is commonly used for classification problems with categorical or non
      negative discrete features Example Suppose we want to predict whether a person has Heart Disease based on
      Smoking Status We have Heart Disease Yes Heart Disease No Total Smoker 40 20 60 Non Smoker 20 70 90 Total
      60 90 150 The Chi Square test compares Observed frequencies what we actually see in the dataset Expected
      frequencies what we would expect if Smoking Status and Heart Disease were independent Hypotheses The Chi
      Square test uses two hypotheses Null hypothesis The feature and the target are independent In our example
      Smoking Status is not associated with Heart Disease Alternative hypothesis The feature and the target are
      associated In our example Smoking Status is associated with Heart Disease Calculate Expected Frequencies
      The expected frequency is calculated as For Smoker Heart Disease Yes For Smoker Heart Disease No For Non
      Smoker Heart Disease Yes For Non Smoker Heart Disease No Therefore Disease Yes Disease No Smoker Observed
      40 Observed 20 Expected 24 Expected 36 Non Smoker Observed 20 Observed 70 Expected 36 Expected 54
      Calculate Chi Square Statistic The formula is where Observed frequency Expected frequency For our example
      Therefore A relatively large Chi Square value indicates that the observed frequencies differ substantially
      from what would be expected if the variables were independent What Does the Chi Square Value Mean A larger
      Chi Square statistic generally indicates stronger evidence of an association between the feature and
      target However when using Chi Square for feature selection it is often more convenient to look at the p
      value For a table Therefore We then use the Chi Square distribution to obtain the p value If we commonly
      reject and conclude that there is statistical evidence of an association between the feature and target 1
      3 Information Gain Information Gain
4. − OLD [539–2251]:
   contributes to the target Decision Trees ID3 Correlation Coefficient Finds features that are highly
   correlated with the class but not with each other Numeric data ANOVA F test Checks whether mean differences
   between groups are statistically significant Continuous features Gini index Example Dataset Weather
   Temperature Play Sunny Hot No Sunny Hot No Overcast Hot Yes Rain Mild Yes Rain Cool Yes Target variable Play
   Possible values Yes or No We want to find out which feature Weather or Temperature is more informative i e
   which helps predict Play better Compute the Gini Index for the Entire Dataset Parent Node The Gini Index
   measures how impure a set is how mixed the target classes are Formula where is the proportion of each class
   Yes No In our dataset Interpretation Gini 0 48 the dataset is moderately impure some Yes some No If it were
   all Yes or all No Gini would be 0 pure Split the Dataset by Each Feature Now check each feature one by one
   For feature Weather we have 3 categories Sunny No No Overcast Yes Rain Yes Yes For feature Temperature we
   have Hot No No Yes Mild Yes Cool Yes Each category becomes a child node We’ll calculate the Gini for each
   child group Compute the Gini Index for Each Subgroup Now compute impurity inside each subgroup For Weather
   Group Yes No Total Gini Sunny 0 2 2 Overcast 1 0 1 Rain 2 0 2 you compute a weighted average to represent the
   impurity after the split Weighted Gini after splitting by Weather For Temperature Group Yes No Total Gini Hot
   1 2 3 Mild 1 0 1 Cool 1 0 1 Weighted Gini after splitting by Temperature Compute the Gini Gain Reduction in
   Impurity Now find out how much impurity was removed when splitting on each feature Feature Parent Gini
   Feature Gini Gini Gain Weather 0 48 0 00 0 48 Temperature 0 48 0 266 0 214 Weather gives the highest
   reduction in impurity 0 48 it’s the most informative feature Rank Features by Gini Gain Now you can rank all
   features based on how much impurity they remove Rank Feature Gini Gain 1 Weather 0 48 2 Temperature 0 214 You
   can now select the top features like top 2 or top 3 for your model Interpret the Results High Gini Gain high
   importance The feature helps classify the target clearly Low Gini Gain less importance The feature doesn’t
   add much predictive power Chi Square Test Test Measures the dependence between categorical features and the
   target variable High Chi square value strong relationship with the target class Formula where observed
   frequency expected frequency Example Use In spam classification the presence of certain words categorical vs
   spam non spam Works well for categorical input and categorical output The Chi Square Test checks whether
   there’s a significant relationship between a feature independent variable and the target class dependent
   variable It’s often used in filter methods for feature selection especially when both variables are
   categorical Scenario Example Let’s say we’re building a model to predict whether a person buys a product Yes
   No based on their age group Age Group Buys Yes Doesn’t Buy No Total Young 20 30 50 Middle aged 30 10 40
   Senior 10 20 30 Total 60 60 120 We want to test Is there a relationship between Age Group and Buying Decision
   Step 1 Define Hypotheses Null Hypothesis H Age group and buying behavior are independent no relationship
   Alternative Hypothesis H Age group and buying behavior are dependent related Step 2 Compute Expected
   Frequencies If there’s no relationship between Age and Buying we expect each cell’s count to follow this rule
   Let’s compute expected frequencies for each cell Age Group Observed Yes Observed No Expected Yes Expected No
   Young 20 30 50 60 120 25 50 60 120 25 Middle aged 30 10 40 60 120 20 40 60 120 20 Senior 10 20 30 60 120 15
   30 60 120 15 Step 3 Apply the Chi Square Formula Where Observed frequency Expected frequency Now compute for
   each cell Group Young Yes 20 25 5 25 1 0 Young No 30 25 5 25 1 0 Middle aged Yes 30 20 10 20 5 0 Middle aged
   No 10 20 10 20 5 0 Senior Yes 10 15 5 15 1 67 Senior No 20 15 5 15 1 67 Now sum all Step 4 Find Degrees of
   Freedom Where number of rows 3 Young Middle aged Senior number of columns 2 Yes No Step 5 Compare with
   Critical Value At significance level 0 05 and df 2 critical value from Chi square table 5 99 Our computed 15
   34 Since 15 34 5 99 we reject the null hypothesis How to Use the Table Find your degrees of freedom df in the
   left column Find your significance level at the top The intersection gives your critical value Compare your
   calculated value to this If calc critical Reject H If calc critical Fail to reject H Step 6 Interpretation
   There is a significant relationship between Age Group and Buying Decision So Age Group is a useful feature
   for classification Summary Table Step Description Result 1 Set hypotheses H independent H dependent 2 Compute
   expected frequencies Based on row column totals 3 Calculate statistic 15 34 4 Determine degrees of freedom 2
   5 Compare with critical value 15 34 5 99 6 Decision Reject H feature is important In Simple Words The Chi
   Square Test measures how much the observed counts differ from the expected counts if there were no
   relationship between the feature and the target The bigger the difference the more important the feature is
   for classification What is Entropy Information Gain Entropy measures the uncertainty or impurity in a dataset
   Formula Where dataset proportion of samples in class number of classes Interpretation Entropy 0 all samples
   belong to one class pure Entropy maximum samples are equally distributed among classes most uncertain 1
   Information Gain IG for Feature Selection Entropy is used in feature selection through Information Gain which
   measures how much a feature reduces uncertainty Formula Where original dataset subset of data where feature
   value weight of the subset Interpretation Higher IG feature reduces uncertainty more more informative 3 Steps
   to Use Entropy as a Feature Selection Tool Step 1 Compute Entropy of the target variable in the full dataset
   Parent Entropy Step 2 Split the dataset by each feature for all possible values or thresholds Step 3 Compute
   Entropy of each subgroup Step 4 Compute weighted average Entropy after split Step 5 Compute Information Gain
   for each feature Step 6 Rank features by IG higher IG more informative step by step feature selection example
   using Entropy Information Gain with your dataset We’ll calculate Entropy and IG for both features Weather and
   Temperature Dataset Weather Temperature Play Sunny Hot No Sunny Hot No Overcast Hot Yes Rain Mild Yes Rain
   Cool Yes Target variable Play Yes No Step 1 Compute Parent Entropy Count of classes Yes 3 No 2 Parent entropy
   0 971 Step 2 Compute Entropy for Weather Split by Weather Weather Yes No Total Entropy Sunny 0 2 2 0 Overcast
   1 0 1 0 Rain 2 0 2 0 Weighted Entropy Step 3 Information Gain for Weather Weather is very informative Step 4
   Compute Entropy for Temperature Split by Temperature Temperature Yes No Total Entropy Hot 1 2 3 Mild 1 0 1 0
   Cool 1 0 1 0 Weighted Entropy Step 5 Information Gain for Temperature Step 6 Compare Features Feature
   Information Gain Weather 0 971 Temperature 0 420 Weather is more informative than Temperature Step 7 Feature
   Selection Decision Select Weather first highest IG Temperature is less informative but could still be used in
   later splits 2 Mutual Information MI Generalization of Information Gain Works for both categorical and
   continuous variables Measures how much knowledge of one variable reduces uncertainty about another Range 0 no
   relation Higher value stronger dependency Used for text classification image recognition and bioinformatics
   Correlation Coefficient Pearson’s r Pearson’s r measures the linear relationship between two variables Where
   values of the feature values of the target mean of the feature and target Interpretation perfect positive
   correlation perfect negative correlation no linear correlation Use in feature selection Features with higher
   absolute value are more strongly correlated with the target more informative 2 Example Dataset Suppose we
   have a dataset of 5 samples Feature X Hours Studied Feature Y Sleep Hours Exam Score 2 8 50 4 7 60 6 6 70 8 5
   80 10 4 90 Target variable Exam Score We want to see which feature Hours Studied or Sleep Hours is more
   informative for predicting Exam Score Step 1 Compute Pearson’s r for Hours Studied vs Exam Score Compute mean
   of each variable Compute numerator X Y X X Y Y X X Y Y 2 50 4 20 80 4 60 2 10 20 6 70 0 0 0 8 80 2 10 20 10
   90 4 20 80 Compute denominator Compute r Perfect positive correlation Hours Studied is highly informative
   Step 2 Compute Pearson’s r for Sleep Hours vs Exam Score X Sleep Y X X Y Y X X Y Y 8 50 3 20 60 7 60 2 10 20
   6 70 1 0 0 5 80 1 10 10 4 90 2 20 40 same as before Denominator Strong negative correlation Sleep Hours is
   informative but inversely related Step 3 Feature Selection Decision Feature Pearson’s r r Hours Studied 1 1
   Sleep Hours 0 943 0 943 Rule Higher r more informative Hours Studied is slightly more informative than Sleep
   Hours absolute correlation Key Points About Using Pearson’s r for Feature Selection Measures linear
   relationship between feature and target Works best with continuous features and continuous targets r close to
   1 strong correlation feature is likely informative r close to 0 weak or no linear relationship feature may be
   irrelevant ANOVA F Test Stands for Analysis of Variance Checks if the mean feature values differ
   significantly across different class labels Intuition If a feature’s mean values vary a lot across classes
   it’s likely useful for classification Works well for continuous features and categorical targets Variance
   Threshold Removes features with low variance i e features that have
   + 2026 [794–1464]:
      provides about the target A feature that significantly reduces uncertainty about the target has high
      information gain For example Feature A Information Gain 0 42 Feature B Information Gain 0 08 Feature A
      would generally be considered more informative than Feature B Information Gain is commonly associated with
      decision tree based feature selection Information Gain for Feature Selection Simple Example Suppose we
      want to predict whether a student will Pass or Fail We have 8 students Student Attendance Study Hours
      Result 1 High High Pass 2 High High Pass 3 High Low Pass 4 High Low Fail 5 Low High Pass 6 Low Low Fail 7
      Low Low Fail 8 Low High Fail We want to answer Which feature is more useful for predicting the Result
      Attendance or Study Hours Step 1 Calculate the initial Entropy There are Pass 4 Fail 4 Therefore So Step 2
      Calculate Information Gain for Attendance Attendance has two groups High Attendance Students 1 4 Result
      Number Pass 3 Fail 1 Entropy Low Attendance Students 5 8 Result Number Pass 1 Fail 3 Therefore Weighted
      Entropy Each group contains 4 out of 8 students Information Gain Step 3 Calculate Information Gain for
      Study Hours High Study Hours Students 1 2 5 8 Result Number Pass 3 Fail 1 Therefore Low Study Hours
      Students 3 4 6 7 Result Number Pass 1 Fail 3 Therefore Weighted Entropy Information Gain Step 4 Compare
      Them Feature Information Gain Attendance 0 189 Study Hours 0 189 In this particular dataset both features
      have the same Information Gain Therefore based only on Information Gain Attendance and Study Hours provide
      the same amount of information about the student's result The basic process to teach students Attendance
      Information Gain 0 189 Compare Study Hours Information Gain 0 189 The general rule is So if Attendance had
      an Information Gain of 0 35 and Study Hours had 0 12 we would select Attendance as the more informative
      feature 1 4 Mutual Information Mutual Information MI measures the amount of information shared between a
      feature and the target It can capture nonlinear relationships which makes it different from simple
      correlation For example If Feature X has a nonlinear relationship with the target correlation might be low
      while mutual information may still be high The main equation for Mutual Information MI is Where the
      feature the target uncertainty entropy of the target before knowing the feature uncertainty of the target
      after knowing the feature Information Gain How much does the feature reduce the uncertainty of the target
      Mutual Information How much information does the feature and target share Example Suppose we want to
      predict whether a student will Pass or Fail We have two features Attendance Study Hours Dataset Student
      Attendance Study Hours Result 1 High High Pass 2 High Low Pass 3 High High Pass 4 High Low Pass 5 Low High
      Fail 6 Low Low Fail 7 Low Low Fail 8 Low High Fail Notice that Attendance perfectly separates the two
      classes High Pass Low Fail But Study Hours does not High sometimes Pass sometimes Fail Low sometimes Pass
      sometimes Fail 1 Mutual Information of Attendance Before using Attendance Pass 4 Fail 4 Therefore After
      knowing Attendance Attendance High All 4 students Pass Attendance Low All 4 students Fail Therefore So 2
      Mutual Information of Study Hours Now consider Study Hours Study Hours High Students Student Result 1 Pass
      3 Pass 5 Fail 8 Fail So Pass 2 Fail 2 Therefore Study Hours Low Students Student Result 2 Pass 4 Pass 6
      Fail 7 Fail Again Pass 2 Fail 2 Therefore Thus and 3 Compare the Two Features Feature Mutual Information
      Attendance 1 0 Study Hours 0 0 Therefore Why Attendance completely determines the result in this example
      High attendance Pass Low attendance Fail But Study Hours provides no useful information here because both
      High and Low study hours contain an equal number of Pass and Fail students 1 5 Variance Threshold This
      method removes features with very low variance If a feature has
5. − OLD [2257–2302]:
   all samples Such features contribute little to classification Simple but effective preprocessing step ReliefF
   Algorithm Assigns weights to features based on how well they distinguish between neighboring samples of
   different classes Works for both categorical and continuous data More advanced filter method that captures
   feature interaction
   + 2026 [1470–1685]:
      every observation it provides little information for distinguishing observations Example Patient Feature 1
      1 2 1 3 1 4 1 5 1 This feature has zero variance and can usually be removed 2 Wrapper Methods Wrapper
      methods use a data mining or machine learning algorithm to evaluate different subsets of features Instead
      of evaluating features individually they ask Which combination of features produces the best model
      performance Common Wrapper Techniques 2 1 Forward Selection Starts with no features Then Add the feature
      that improves performance the most Add another feature that provides the next largest improvement Continue
      until a stopping condition is reached Example Start No features Add Glucose Add BMI Add Age Add Blood
      Pressure Final subset 2 2 Backward Elimination Starts with all features Then Train the model using all
      features Remove the least useful feature Retrain the model Continue removing features Example All features
      Remove Patient ID Remove Skin Thickness Remove Insulin Final subset 2 3 Recursive Feature Elimination RFE
      RFE repeatedly trains a model and removes the least important features For example 10 features Train model
      Remove least important feature 9 features Train model Remove least important feature 5 selected features
      RFE can be used with algorithms such as Logistic Regression SVM and Random Forest depending on the
      implementation 3 Embedded Methods
6. − OLD [2309–2514]:
   model training More efficient than wrapper methods Examples Method Algorithm Example Description LASSO L1
   Regularization Linear Logistic Regression Shrinks some coefficients to zero feature removal Tree based
   Importance Random Forest XGBoost Features ranked by information gain or Gini importance Elastic Net Combines
   L1 and L2 regularization Balances between feature elimination and coefficient shrinkage Wrapper Methods Use a
   predictive model to evaluate the importance of subsets of features Computationally expensive but often more
   accurate Process Select a subset of features Train a model and test accuracy Add remove features and repeat
   Examples Method Description Forward Selection Start with no features add one at a time Backward Elimination
   Start with all features remove one at a time Recursive Feature Elimination RFE Recursively remove least
   important features e g using SVM or Logistic Regression Classification algorithms Decision Trees Classifier A
   Decision Tree is a tree structured model used for classification and prediction It splits data into branches
   based on feature values leading to a decision outcome class label or numeric prediction Example Simple If you
   were deciding whether to play tennis IF Outlook Sunny AND Humidity 75 Don’t Play IF Outlook Overcast Play IF
   Outlook Rainy AND Wind Weak Play Each rule comes from a path in the tree
   + 2026 [1692–5712]:
      the model training process Therefore feature selection is part of the learning algorithm itself Common
      Embedded Techniques 3 1 LASSO Regression LASSO uses L1 regularization It adds a penalty to the model The
      L1 penalty can force some coefficients to become exactly zero For example Feature Coefficient Glucose 0 82
      BMI 0 31 Age 0 15 Insulin 0 Patient ID 0 Features with coefficients equal to zero can be removed 3 2
      Decision Trees Decision trees select features when constructing the tree For example Glucose High Low BMI
      Age The tree gives greater importance to features that provide useful splits Feature importance can then
      be used for feature selection 3 3 Random Forest Feature Importance Random Forest can calculate feature
      importance based on how much features contribute to reducing impurity or depending on the method how much
      they affect prediction performance Example Feature Importance Glucose 0 31 BMI 0 18 Age 0 14 Blood
      Pressure 0 09 Patient ID 0 00 Features with very low importance may be removed Comparison of the Three
      Main Methods Method Basic Idea Model Required Speed Filter Evaluate features using statistical measures No
      Fast Wrapper Evaluate feature subsets using a model Yes Slow Embedded Select features during model
      training Yes Medium Fast Simple Example Suppose we have 20 features and want to select the most useful
      ones Filter Calculate statistical scores select top 8 features Wrapper Try different combinations train
      model choose the subset producing the best performance Embedded Train a model model automatically assigns
      zeros feature coefficients or importance select important features Key Difference Filter methods select
      features before model training Wrapper methods select features by repeatedly evaluating a model Embedded
      methods select features as part of model training Classification in Data Mining 1 Introduction to
      Classification 1 1 Definition of Classification Classification is one of the most important techniques in
      Data Mining and Machine Learning It is used to assign a data record to one of a set of predefined classes
      Simple Definition Classification is the process of learning from previously labeled data and using the
      learned knowledge to assign a class to new data For example a hospital may want to determine whether a
      patient has a particular disease The possible classes could be Disease No Disease The classification model
      learns from previous patients and then predicts the class of a new patient 1 2 Why Classification Is
      Important Classification is important because many real world problems require us to make decisions based
      on available data For example Healthcare Predict whether a patient has a disease Banking Predict whether a
      customer is likely to default on a loan Education Predict whether a student will pass or fail
      Cybersecurity Determine whether network traffic is normal or malicious Email Determine whether an email is
      spam or not spam Business Predict whether a customer will leave a company Therefore classification is
      widely used for prediction and decision making 1 3 Classification as Supervised Learning Classification is
      a type of supervised learning The term supervised means that the training data contains the correct
      answers For example consider a dataset containing patient information Age Glucose BMI Diabetes 25 110 23 5
      No 45 180 31 2 Yes 52 160 29 8 Yes 30 95 22 1 No The first three columns describe the patients The last
      column contains the known class The algorithm studies these examples and learns patterns that can be used
      to classify new patients Basic Idea Labeled Data Classification Algorithm Classification Model New Data
      Predicted Class 1 4 Applications of Classification Classification is used in many areas Medical
      Applications Disease diagnosis Cancer classification Patient risk classification Financial Applications
      Fraud detection Credit risk classification Loan approval Educational Applications Student performance
      prediction Student dropout prediction Pass and fail prediction Cybersecurity Applications Malware
      classification Intrusion detection Phishing detection Business Applications Customer churn prediction
      Customer response prediction Product classification Text Mining Applications Spam detection Sentiment
      classification Document classification Image Applications Object classification Face recognition Medical
      image classification 2 Basic Concepts of Classification Before studying classification algorithms students
      need to understand several important terms 2 1 Dataset A dataset is a collection of data records For
      example a medical dataset may contain information about thousands of patients A student dataset may
      contain information about Student age Attendance Grades Study hours Final result 2 2 Instance An instance
      is one individual record in a dataset For example One patient is one instance One student is one instance
      One email is one instance In a table an instance is usually represented by one row 2 3 Feature A feature
      is an attribute that describes an instance For example patient features may include Age Weight Blood
      pressure Glucose BMI Features are also called Attributes Variables Predictors Features are used by the
      classification model to make predictions 2 4 Class Label The class label is the category that we want to
      predict Examples Diabetes Yes No Cancer Benign Malignant Student Performance Pass Fail Email Spam Not Spam
      The class label is also commonly called the target variable 2 5 Training Data Training data is the data
      used to teach the classification algorithm It contains Features Known class labels The algorithm examines
      the training data and learns patterns 2 6 Validation Data Validation data is used during model development
      It can help us Select between different models Tune model settings Detect overfitting Choose the best
      model Validation data is particularly useful when developing more complex models 2 7 Test Data Test data
      is used to evaluate the final classification model The model should not use the test data during training
      The purpose is to determine how well the model performs on unseen data 3 How Classification Works
      Classification normally involves several stages 3 1 Model Training First we provide the algorithm with
      training data For example Study Hours Attendance Previous Grade Result 2 60 50 Fail 4 75 65 Pass 6 90 80
      Pass 1 50 40 Fail 5 85 75 Pass The algorithm examines the relationship between the features and the class
      It tries to learn patterns that distinguish one class from another 3 2 Model Testing After training the
      model is evaluated using data that it has not seen during training For example Study Hours Attendance
      Previous Grade Actual Result 3 70 55 Fail 6 88 82 Pass The model predicts the results We then compare the
      predictions with the actual results 3 3 Classification of New Data Once we are satisfied with the model's
      performance we can use it to classify new records For example New student Study hours 5 Attendance 88
      percent Previous grade 78 The model may predict Pass The model made this prediction based on patterns
      learned from previous students 3 4 Example of a Classification Problem Consider a hospital that wants to
      classify patients into High Risk Low Risk The hospital has historical patient data Features may include
      Age Blood pressure Cholesterol Weight Previous medical history The model learns from previous patients
      When a new patient arrives the model predicts High Risk or Low Risk 4 Types of Classification There are
      several types of classification problems 4 1 Binary Classification Binary classification contains two
      classes Examples Email Spam Not Spam Medical Diagnosis Disease No Disease Education Pass Fail Banking
      Fraud Not Fraud Binary classification is one of the most common types of classification 4 2 Multiclass
      Classification Multiclass classification contains more than two classes For example an image
      classification system may classify images into Cat Dog Horse Bird Another example is disease
      classification Diabetes Heart Disease Kidney Disease Healthy The model normally assigns one class to each
      instance 4 3 Multilabel Classification In multilabel classification one instance can belong to more than
      one class at the same time For example a research paper could be classified as Artificial Intelligence
      Machine Learning Data Mining The paper can belong to all three categories Difference Multiclass One
      instance One class Multilabel One instance Multiple classes 4 4 Classification and Regression
      Classification and regression are both supervised learning techniques but they predict different types of
      outputs Classification Predicts a category Example Patient Disease or No Disease Regression Predicts a
      numerical value Example Patient Expected blood glucose level Therefore Classification predicts categories
      while regression predicts numerical values 4 5 Classification and Clustering Classification and clustering
      are often confused They are different techniques Classification Clustering Supervised learning
      Unsupervised learning Uses labeled data Uses unlabeled data Classes are already known Groups are
      discovered Used for prediction Used to discover patterns Example If we know that emails are Spam Not Spam
      and we train a model to classify new emails this is classification If we have thousands of emails without
      labels and want to discover groups of similar emails this is clustering 5 Classification Algorithms There
      are many classification algorithms The most important algorithms include Decision Tree Naive Bayes K
      Nearest Neighbors Support Vector Machine Logistic Regression Random Forest Neural Networks 6
      Classification Model Evaluation After building a classification model we need to determine how well it
      performs Model evaluation is important because a model that performs well on training data may not
      necessarily perform well on new data Important evaluation measures include Confusion Matrix Accuracy
      Precision Recall Specificity F1 score ROC Curve AUC 6 1 Confusion Matrix A confusion matrix shows the
      correct and incorrect predictions made by a classification model For binary classification Predicted
      Positive Predicted Negative Actual Positive True Positive False Negative Actual Negative False Positive
      True Negative 6 2 True Positive The actual class is positive The model also predicts positive Example A
      patient has cancer The model predicts cancer This is a True Positive 6 3 True Negative The actual class is
      negative The model also predicts negative Example A patient does not have cancer The model predicts no
      cancer This is a True Negative 6 4 False Positive The actual class is negative The model predicts positive
      Example A patient does not have cancer The model predicts cancer This is a False Positive This can be
      considered a false alarm 6 5 False Negative The actual class is positive The model predicts negative
      Example A patient has cancer The model predicts no cancer This is a False Negative In some medical
      applications false negatives can be particularly serious 6 6 Accuracy Accuracy measures the percentage of
      all predictions that are correct For example Suppose there are 100 patients The model correctly classifies
      95 patients The accuracy is 95 percent Accuracy is easy to understand but it should not always be used
      alone 6 7 Precision Precision answers the question When the model predicts positive how often is it
      correct Formulas For example The model predicts that 100 patients have a disease Only 90 actually have the
      disease The precision is 90 percent Precision is important when false positive predictions are costly 6 8
      Recall Recall answers the question Of all the cases that are actually positive how many did the model
      correctly identify For example There are 100 patients who actually have a disease The model correctly
      identifies 95 of them The recall is 95 percent Recall is especially important when missing a positive case
      can have serious consequences 6 9 Specificity Specificity answers the question Of all the cases that are
      actually negative how many did the model correctly identify For example There are 100 healthy patients The
      model correctly identifies 90 of them as healthy The specificity is 90 percent 6 10 F1 Score F1 score
      combines precision and recall into one measure It is particularly useful when The dataset is imbalanced
      Both false positives and false negatives are important A high F1 score means that the model has a good
      balance between precision and recall 6 11 ROC Curve The ROC curve is used mainly for binary classification
      It evaluates the model at different decision thresholds It considers two important aspects How well the
      model identifies positive cases How often the model incorrectly identifies negative cases as positive A
      model with better separation between the classes generally has a better ROC curve 6 12 AUC AUC means Area
      Under the ROC Curve It provides a single value that summarizes the model's ability to distinguish between
      classes Generally AUC General Interpretation 0 50 Random performance 0 60 0 70 Poor 0 70 0 80 Acceptable 0
      80 0 90 Good 0 90 1 00 Excellent These values should be considered general guidelines rather than strict
      rules 7 Problems in Classification Classification models can face several problems The most important are
      Class imbalance Overfitting Underfitting Irrelevant features Missing data Noisy data 7 1 Class Imbalance
      Class imbalance occurs when one class contains significantly more records than another For example Class
      Number Healthy 9 000 Disease 1 000 The dataset is imbalanced Suppose a model predicts every patient as
      healthy The model would achieve 90 percent accuracy However it would fail to identify any patient with the
      disease Therefore High accuracy does not always mean that a classification model is good 7 2 Overfitting
      Overfitting occurs when the model learns the training data too closely For example Training accuracy 99
      percent Testing accuracy 70 percent The large difference suggests that the model may have learned the
      training data rather than learning general patterns Causes Model is too complex Dataset is too small Too
      many features Noisy data Insufficient regularization 7 3 Underfitting Underfitting occurs when the model
      is too simple to learn the important patterns in the data For example Training accuracy 65 percent Testing
      accuracy 63 percent The model performs poorly on both training and testing data Possible solutions include
      Using a more appropriate algorithm Adding useful features Reducing excessive regularization Improving the
      quality of the data 7 4 Irrelevant Features Not every feature in a dataset is useful For example suppose
      we want to predict whether a patient has diabetes Useful features may include Age Glucose BMI Blood
      pressure An unrelated feature may add noise without helping the prediction Too many irrelevant features
      can Increase complexity Increase training time Reduce model performance Increase the risk of overfitting 7
      5 Missing Data Real world datasets often contain missing values For example Age Glucose BMI 45 180 31 52
      Missing 29 30 95 22 Missing data must be handled appropriately before training many classification models
      Possible approaches include Removing records Replacing missing values Using statistical imputation Using
      model based imputation The appropriate approach depends on the dataset and the reason for the missing
      values 7 6 Noisy Data Noise refers to incorrect inconsistent or unnecessary information in the dataset
      Examples include Incorrect measurements Typographical errors Incorrect labels Extreme values caused by
      measurement errors Data cleaning is an important step before classification 8 Improving Classification
      Performance Several techniques can improve classification performance 8 1 Data Preprocessing Data
      preprocessing prepares the dataset before model training It may include Handling missing values Removing
      duplicates Correcting errors Encoding categorical data Scaling numerical features Good preprocessing can
      significantly affect model performance 8 2 Feature Selection Feature selection means choosing the most
      useful features Suppose a dataset contains 100 features Only 20 may be strongly related to the target
      class Using the most useful features can Reduce complexity Reduce training time Reduce overfitting Improve
      interpretability Sometimes improve prediction performance Common techniques include Information Gain Chi
      Square Correlation Mutual Information Recursive Feature Elimination Feature Importance 8 3 Feature Scaling
      Feature scaling ensures that numerical features have comparable scales For example Age may range from 18
      to 80 Income may range from 1 000 to 100 000 The large difference in scale can affect algorithms such as
      KNN SVM Logistic Regression Neural Networks Common scaling methods include Standardization Min Max Scaling
      Robust Scaling 8 4 Handling Class Imbalance Several techniques can be used Oversampling Increase the
      number of minority class examples Undersampling Reduce the number of majority class examples SMOTE SMOTE
      creates synthetic examples for the minority class Class Weights Give greater importance to minority class
      errors Appropriate Evaluation Measures Use Precision Recall F1 score Specificity AUC rather than relying
      only on accuracy 8 5 Cross Validation Cross validation is used to obtain a more reliable estimate of model
      performance In five fold cross validation the dataset is divided into five parts The model is trained and
      evaluated several times Each part is used as the validation set while the remaining parts are used for
      training The results are then averaged Cross validation is especially useful when the available dataset is
      not very large 8 6 Hyperparameter Tuning Classification algorithms contain settings called hyperparameters
      Examples include KNN Number of neighbors Decision Tree Maximum tree depth Random Forest Number of trees
      SVM Kernel and other model settings Hyperparameter tuning attempts to find suitable values for these
      settings Common methods include Grid Search Random Search Bayesian Optimization 8 7 Ensemble Methods An
      ensemble method combines multiple models to produce a stronger prediction Examples include Random Forest
      Gradient Boosting AdaBoost XGBoost The main idea is that combining several models can sometimes produce
      better and more stable results than using one model alone 9 Classification Workflow A complete
      classification project normally follows a sequence of steps Step 1 Data Collection Collect the required
      dataset Step 2 Data Understanding Study Number of records Features Classes Data types Class distribution
      Step 3 Data Cleaning Handle Missing values Duplicate records Incorrect values Noise Step 4 Data
      Preparation Perform appropriate Encoding Scaling Transformation Step 5 Feature Selection Select useful
      features Step 6 Data Splitting Divide the data into appropriate training validation and testing sets Step
      7 Model Training Train one or more classification algorithms Step 8 Model Evaluation Evaluate the models
      using appropriate performance measures Step 9 Model Tuning Improve the selected model by tuning its
      hyperparameters Step 10 Final Prediction Use the final model to classify new unseen data 10 Comparison of
      Classification Algorithms Algorithm Main Strength Main Weakness Decision Tree Easy to understand Can
      overfit Naive Bayes Fast and simple Strong independence assumption KNN Simple and intuitive Can be slow
      with large datasets SVM Good for complex boundaries Can require careful parameter tuning Logistic
      Regression Simple and interpretable Limited for complex relationships Random Forest Robust and accurate
      Less interpretable Neural Network Powerful for complex data Requires careful training There is no single
      classification algorithm that is best for every dataset The best choice depends on Dataset size Number of
      features Data type Class distribution Complexity of the problem Required interpretability Computational
      resources 11 Applications of Classification Classification has many real world applications 11 1
      Healthcare Examples Disease diagnosis Cancer classification Patient risk prediction Medical image
      classification 11 2 Banking and Finance Examples Fraud detection Loan approval Credit risk classification
      Customer risk assessment 11 3 Education Examples Student performance prediction Dropout prediction Pass
      and fail prediction Student risk classification 11 4 Cybersecurity Examples Intrusion detection Malware
      classification Phishing detection Network traffic classification 11 5 Business Examples Customer churn
      prediction Customer response prediction Product classification Customer risk classification 11 6 Text
      Mining Examples Spam detection Sentiment analysis News classification Document classification 11 7 Image
      Classification Examples Face recognition Object classification Medical image classification Animal
      classification 12 Practical Classification Example Breast Cancer Classification Consider a breast cancer
      dataset The dataset contains information about breast tumors Features Examples include Tumor size Cell
      characteristics Texture Shape Other medical measurements Classes The target class may be Benign Malignant
      Practical Process Step 1 Load the dataset Step 2 Examine the features and classes Step 3 Check for missing
      values Step 4 Check whether the classes are balanced Step 5 Prepare the features Step 6 Divide the data
      into training and testing sets Step 7 Train several classification algorithms Logistic Regression Decision
      Tree KNN SVM Random Forest Step 8 Evaluate each model Use Accuracy Precision Recall Specificity F1 score
      AUC Step 9 Compare the results Step 10 Select the most appropriate model The best model should not
      necessarily be the model with the highest accuracy For a medical application recall and specificity may be
      particularly important LECTURE RULE BASED CLASSIFIERS Course Data Mining Topic Classification Techniques
      Level Master's Students 1 Introduction Classification is a supervised learning technique in data mining
      used to assign data objects to predefined classes A model learns from labeled training data and uses that
      knowledge to predict the class of new data A rule based classifier uses a collection of IF THEN rules to
      assign class labels Example IF attendance is high AND the exam mark is at least 50 THEN the student passes
      2 Definition and Structure A rule based classifier represents classification knowledge in the form IF
      condition THEN class Antecedent the IF part containing the conditions that must be satisfied Consequent
      the THEN part containing the predicted class Example IF Age 30 AND Income High THEN Loan Status Approved
      Here Age 30 AND Income High is the antecedent and Loan Status Approved is the consequent 3 Conditions and
      Logical Operators A rule can contain one or more conditions connected by logical operators such as AND and
      OR Example IF Attendance 75 AND Exam Mark 50 THEN Result Pass The AND operator means both conditions must
      be true for the rule to apply An OR operator means at least one of its connected conditions must be true 4
      How Rule Based Classification Works 1 Prepare the dataset by collecting and cleaning the data 2 Generate
      IF THEN rules from the training data 3 Evaluate how accurately the rules classify training examples 4
      Apply the rules to a new data record 5 Assign the predicted class based on the matching rule or rules
      Example dataset Student Attendance Exam mark Result S1 90 80 Pass S2 85 65 Pass S3 60 45 Fail S4 50 35
      Fail S5 80 40 Fail Possible rules Rule 1 IF Exam Mark 50 THEN Result Pass Rule 2 IF Exam Mark 50 THEN
      Result Fail Student S1 has a mark of 80 so Rule 1 predicts Pass Student S3 has a mark of 45 so Rule 2
      predicts Fail 5 Types of Rule Based Classifiers 5 1 Ordered Rules Rules are evaluated in a specific
      sequence The first matching rule determines the predicted class Therefore rule order can affect the result
      when multiple rules match 5 2 Unordered Rules Rules do not necessarily have a fixed priority If multiple
      rules match the classifier may use voting rule quality or another conflict resolution strategy 5 3 Default
      Rule A default rule handles a record when no explicit rule matches Rule 1 IF Exam Mark 50 THEN Result Pass
      Rule 2 IF Exam Mark 40 THEN Result Fail Default Result Fail A mark of 45 matches neither explicit rule so
      the default rule assigns Fail 6 Rule Coverage and Rule Accuracy 6 1 Rule Coverage Coverage is the
      proportion of records that satisfy a rule's conditions Coverage R Number of records satisfying R Total
      number of records Example If 40 of 100 students satisfy a rule coverage 40 100 0 40 or 40 6 2 Rule
      Accuracy Rule accuracy is the proportion of records covered by a rule that belong to the class predicted
      by that rule Accuracy R Correctly classified covered records All records covered by R Example If a rule
      covers 40 students and correctly classifies 36 accuracy 36 40 0 90 or 90 Coverage measures how many
      records a rule applies to Accuracy measures how often the rule predicts the correct class among those
      records 7 Conflict Resolution A conflict occurs when two or more rules match the same record but predict
      different classes Rule 1 IF Attendance 75 THEN Result Pass Rule 2 IF Exam Mark 50 THEN Result Fail A
      student with 80 attendance and a mark of 40 matches both rules which predict different classes Common
      conflict resolution approaches include Rule priority prefer the rule with higher priority Rule ordering
      use the first matching rule Rule quality select the rule with stronger performance on training data Voting
      matching rules vote for a class Default class use a predefined class when needed 8 How Classification
      Rules Are Generated 8 1 Direct Rule Generation Some algorithms learn rules directly from training data by
      identifying conditions that frequently correspond to particular classes 8 2 Extracting Rules from Decision
      Trees A decision tree can be converted into IF THEN rules Each path
7. − OLD [2521–3795]:
   node Structure of a Decision Tree Element Description Root Node Represents the entire dataset first decision
   point e g Outlook Internal Nodes Represent decisions based on attributes e g Humidity Wind Branches Represent
   possible outcomes of each decision Leaf Nodes Represent the final class or prediction result How Decision
   Trees Work They are built using a top down recursive divide and conquer approach 1 Start with the full
   dataset 2 Select the best attribute to split data using criteria like Information Gain or Gini Index 3 Split
   data into subsets based on attribute values 4 Repeat the process for each subset until All samples in a node
   belong to one class or No more attributes remain Splitting Criteria Attribute Selection Measures When
   building a tree we must choose which attribute to split on at each step Here are the most popular measures
   Criterion Used In Description Information Gain ID3 C4 5 Based on reduction in entropy purity of node Gain
   Ratio C4 5 Adjusts information gain to avoid bias toward many valued attributes Gini Index CART Measures
   impurity smaller Gini purer node Chi Square CHAID Statistical test for independence between attribute and
   class Entropy and Information Gain Example Entropy measures uncertainty impurity Information Gain measures
   how much entropy is reduced after splitting The attribute with the highest information gain is chosen for the
   split Stopping Conditions A decision tree stops growing when All records in a node belong to one class No
   remaining attributes to split The tree reaches a predefined maximum depth Further splits do not improve
   accuracy significantly Tree Pruning Pruning helps avoid overfitting by removing unnecessary branches Type
   Description Pre pruning Early Stopping Stop growing when improvement is small Post pruning Grow the full tree
   first then remove weak branches using validation data Example Decision Tree Play Tennis Outlook Sunny
   Overcast Rainy Humidity Yes Wind High Normal Weak Strong No Yes Yes No Advantages of Decision Trees Easy to
   interpret like human reasoning IF THEN rules No data normalization needed handles numeric and categorical
   features Handles missing values gracefully Can handle both classification and regression tasks Disadvantages
   Overfitting if tree grows too deep Unstable small data changes can alter structure Biased toward attributes
   with many distinct values unless using Gain Ratio May produce complex trees for noisy data Popular Decision
   Tree Algorithms Algorithm Main Characteristics ID3 Iterative Dichotomiser 3 Uses Information Gain handles
   categorical data only C4 5 Extension of ID3 handles continuous data and pruning CART Classification and
   Regression Trees Uses Gini Index supports classification and regression CHAID Uses Chi Square good for
   categorical predictors Random Forest Ensemble of many decision trees improves accuracy Decision Trees vs Rule
   Based Classifiers Aspect Decision Tree Rule Based Classifier Representation Hierarchical tree Flat set of IF
   THEN rules Rule Extraction Each path rule Directly written as rules Conflicts No conflicts one path Possible
   overlapping rules Interpretability Easy Easier if few rules Applications of Decision Trees Medical diagnosis
   Fraud detection Credit risk assessment Marketing segmentation Customer churn prediction Fault detection in
   systems Summary Concept Description Definition Tree based model for classification regression Splitting
   Criteria Information Gain Gain Ratio Gini Index Advantages Simple interpretable non parametric Disadvantages
   Overfitting instability Popular Algorithms ID3 C4 5 CART In short Decision Trees are powerful interpretable
   models that make predictions by recursively splitting data based on attribute values Each leaf represents a
   final decision and each path can be easily understood as a logical rule step by step example of building a
   Decision Tree using a small dataset We’ll use Entropy Information Gain as the splitting criterion Dataset
   Weather Temperature Play Sunny Hot No Sunny Hot No Overcast Hot Yes Rain Mild Yes Rain Cool Yes Target
   variable Play Yes No Step 1 Compute Parent Entropy Count of classes Yes 3 No 2 Parent entropy 0 971 Step 2
   Compute Information Gain for Each Feature 2a Feature Weather Split by Weather Weather Yes No Total Entropy
   Sunny 0 2 2 0 Overcast 1 0 1 0 Rain 2 0 2 0 Weighted Entropy Information Gain 2b Feature Temperature Split by
   Temperature Temperature Yes No Total Entropy Hot 1 2 3 0 918 Mild 1 0 1 0 Cool 1 0 1 0 Weighted Entropy
   Information Gain Step 3 Choose Root Node Weather has higher IG 0 971 0 420 becomes root node Step 4 Split
   Dataset by Root Node Root Weather Sunny 2 samples both No leaf node No Overcast 1 sample Yes leaf node Yes
   Rain 2 samples both Yes leaf node Yes Step 5 Final Decision Tree Weather Sunny Overcast Rain No Yes Yes The
   tree perfectly classifies all samples Notes If a split does not perfectly separate classes you would repeat
   the splitting process recursively for each child node You can use Gini Index instead of Entropy it’s another
   impurity measure Decision Trees are easy to visualize and interpret Rule Based Classifiers Rule based
   classifiers are classification systems that use a set of IF THEN rules to make predictions Each rule defines
   a relationship between feature values conditions and a class label conclusion Example Rule 1 IF age 50 AND
   smoker yes THEN class high risk Rule 2 IF age 50 AND smoker no THEN class low risk Each rule represents a
   small interpretable decision pattern learned from data Structure of a Rule A classification rule has two
   parts IF Condition the antecedent THEN Class the consequent Example IF Outlook Sunny AND Humidity 75 THEN
   Play No How Rule Based Classifiers Work They work in two main phases 1 Rule Generation The system analyzes
   the training data and generates a set of classification rules There are two major approaches Approach
   Description Direct from data Rules are learned directly from training data without building another model
   first Example RIPPER CN2 Indirect from another model Rules are extracted from another model like a decision
   tree Example C4 5 rules extracted from decision trees 2 Rule Pruning and Ordering Pruning removes unnecessary
   or conflicting rules to improve generalization Ordering determines which rule should be applied first when
   multiple rules match Rule Evaluation Measures When learning rules we want them to be both accurate and
   general Key metrics used Measure Meaning Coverage How many instances the rule applies to Accuracy How often
   the rule correctly predicts the class Support Number or proportion of instances that satisfy the rule
   Confidence Conditional probability that the rule’s conclusion is correct given the condition Rule Ordering
   Strategies When multiple rules may apply to a new instance the classifier must decide which rule to use Type
   Description Ordered Rule List Decision List Rules are evaluated in order the first matching rule is used
   Unordered Rule Set All matching rules vote and the class with the highest total votes is chosen Example
   Weather Dataset Outlook Temperature Humidity Wind Play Sunny Hot High Weak No Overcast Cool Normal Strong Yes
   Generated Rules 1 IF Outlook Overcast THEN Play Yes 2 IF Outlook Sunny AND Humidity High THEN Play No 3 IF
   Wind Weak AND Humidity Normal THEN Play Yes Advantages of Rule Based Classifiers Easy to Understand Rules are
   human readable and explainable Transparency Each prediction can be explained by a simple rule Flexible Can
   easily add remove or modify rules Good for Categorical Data Naturally handles symbolic or discrete attributes
   Limitations Overfitting Risk Too many specific rules may not generalize well Conflicts Different rules might
   predict different classes for the same input Scalability Generating many rules for high dimensional data can
   be computationally expensive Continuous Features Need to be discretized before rule generation Common Rule
   Based Classifiers Algorithm Description RIPPER Rule based classifier focusing on high accuracy and pruning
   redundant rules PART Combines decision trees and rules
   + 2026 [5719–5839]:
      becomes a rule IF Exam Mark 50 THEN Result Pass IF Exam Mark 50 THEN Result Fail 8 3 Sequential Covering
      Sequential covering generates rules one at a time 6 Find a rule that correctly classifies a group of
      training records 7 Add the rule to the rule set 8 Remove or set aside covered records depending on the
      algorithm 9 Repeat to learn additional rules 10 Stop when a suitable stopping condition is reached RIPPER
      is an example of a rule learning algorithm that uses a sequential covering approach 9 Common Algorithms
      Algorithm Main idea OneR Builds a simple classifier using one attribute RIPPER Learns rules using
      sequential covering and simplifies them CN2 Learns classification rules using heuristic search PART
8. − OLD [3802–3822]:
   CN2 Classical algorithm using beam search for rule generation C4 5 Rules Extracts IF THEN rules from C4 5
   decision trees
   + 2026 [5846–5951]:
      10 Advantages Interpretability rules are usually easy to understand Transparency a prediction can be
      explained by showing the matching rule Flexibility rules can combine multiple attributes Knowledge
      representation rules express knowledge in a human readable form Practical implementation simple rules can
      be implemented with conditional statements 11 Limitations Conflicting rules may predict different classes
      Complex datasets may require a large number of rules Overfitting can occur when rules describe training
      examples too specifically Some records may not match any explicit rule Large rule sets can be difficult to
      maintain Rule pruning rule ordering default classes and validation on unseen data can help address these
      limitations 12
9. − OLD [3829–3992]:
   Aspect Rule Based Classifiers Decision Trees Representation Set of IF THEN rules Hierarchical tree
   Readability Easier for humans Slightly less direct Conflict Handling Rules may overlap Each instance follows
   one path Model Type Flat structure Hierarchical structure Summary Feature Description Definition A
   classification approach using IF THEN rules Learning Method Direct from data or extracted from trees
   Advantages Interpretable flexible transparent Limitations Overfitting rule conflicts Examples RIPPER CN2 PART
   C4 5 Rules In short Rule based classifiers are a simple yet powerful way to classify data using interpretable
   logical rules They are especially valuable when explainability is as important as accuracy Naive Bayes
   algorithm The Naive Bayes algorithm is a probabilistic machine learning classifier based on Bayes Theorem
   with a strong assumption that the features are independent of each other hence naive Despite this
   simplification it performs surprisingly well in many real world applications especially in text
   classification like spam detection or sentiment analysis Let’s break it down clearly 1 Bayes Theorem The
   algorithm
   + 2026 [5958–6298]:
      Feature Rule Based Classifier Decision Tree Representation IF THEN rules Tree structure Prediction
      Evaluate applicable rules Follow a path from root to leaf Interpretability Often clear for small rule sets
      Often clear for small trees Overlapping conditions Possible One path is followed in a standard tree
      Generation Learned directly or extracted Built by recursively splitting data Complexity May contain
      overlapping rules May contain many branches and leaves A decision tree can be converted into rules but a
      rule based classifier does not have to originate from a decision tree 13 Practical Example Loan Approval
      Suppose a bank classifies loan applications as Approved or Rejected using income and credit history Rule 1
      IF Credit History Good AND Income High THEN Loan Status Approved Rule 2 IF Credit History Poor THEN Loan
      Status Rejected Rule 3 IF Income Low THEN Loan Status Rejected Default rule Loan Status Rejected An
      applicant with good credit history and high income satisfies Rule 1 and is predicted as Approved An
      applicant with poor credit history matches Rule 2 and is predicted as Rejected In real lending systems
      rules must be validated and comply with applicable regulations 14 Summary A rule based classifier is a
      supervised classification technique that uses IF THEN rules to assign class labels Each rule contains an
      antecedent conditions and a consequent predicted class Key concepts include rule generation and
      application ordered and unordered rules coverage and accuracy conflict resolution default classes and the
      advantages and limitations of rule based classification Rule based classifiers are particularly useful
      when understanding why a prediction was made is as important as obtaining the prediction itself Important
      distinction During training the output labels guide the creation and selection of rules During prediction
      the output is unknown so the classifier applies the learned rules to the input attributes to predict the
      class NAIVE BAYES ALGORITHM 1 Introduction Naive Bayes is a supervised machine learning algorithm used for
      classification It predicts the class of a new record by calculating the probability that the record
      belongs to each possible class It
10. − OLD [3998–4062]:
   Where class label feature vector probability of class given features posterior prior probability of class
   likelihood of features given the class probability of features can be ignored for comparison between classes
   2 Naive Assumption Naive Bayes assumes all features are independent given the class so This simplification
   makes computation much easier 3 Classification Rule To classify a new sample Compute probability for each
   class Pick
   + 2026 [6304–6523]:
      and assumes that input attributes are conditionally independent given the class Applications include email
      spam detection sentiment analysis medical diagnosis document classification and weather prediction 2 Bayes
      Theorem Bayes theorem calculates the probability of a class given observed evidence P C X P X C x P C P X
      Where P C X Posterior probability probability of class C given attributes X P X C Likelihood probability
      of observing X when the class is C P C Prior probability probability of class C before considering the
      attributes P X Evidence overall probability of observing X Observed attributes update our estimate of
      which class is most likely 3 Why Is It Called Naive Bayes It is called naive because it assumes input
      attributes are conditionally independent when the class is known For example a student classifier might
      use attendance study hours and assignment completion to predict Pass or Fail Naive Bayes assumes these
      attributes are conditionally independent given the result Real attributes may be related but the algorithm
      can still perform well 4 How Naive Bayes Works The algorithm generally follows these steps 11 Collect
      labeled training data 12 Calculate the prior probability of each class 13 Calculate the likelihood of each
      attribute value for each class 14 Calculate a score or posterior probability for each candidate class 15
      Predict
11. − OLD [4068–4519]:
   probability 4 Types of Naive Bayes Depending on feature types there are several variations Gaussian Naive
   Bayes for continuous numeric features assumes normal distribution Multinomial Naive Bayes for discrete count
   features common in text classification Bernoulli Naive Bayes for binary features yes no 0 1 5 Example Text
   Classification Suppose you want to classify emails as Spam or Not Spam Features presence absence of words
   like win free offer Prior probabilities Likelihoods probabilities of each word appearing in spam or not spam
   emails Compute posterior for each class and choose the higher one Advantages Simple and fast Works well with
   high dimensional data Requires less training data Limitations Assumes feature independence rarely true in
   real data Can perform poorly if features are strongly correlated Naive Bayes Example Play Tennis Dataset
   Outlook Temperature Humidity Wind PlayTennis Sunny Hot High Weak No Sunny Hot High Strong No Overcast Hot
   High Weak Yes Rain Mild High Weak Yes Rain Cool Normal Weak Yes Rain Cool Normal Strong No Overcast Cool
   Normal Strong Yes Sunny Mild High Weak No Sunny Cool Normal Weak Yes Rain Mild Normal Weak Yes New day to
   predict Outlook Sunny Temperature Cool Humidity High Wind Strong Step 1 Prior Probabilities Step 2
   Likelihoods Feature Probabilities For class Yes Feature Probability Outlook Sunny 2 6 0 33 Temperature Cool 2
   6 0 33 Humidity High 3 6 0 5 Wind Strong 2 6 0 33 For class No Feature Probability Outlook Sunny 3 4 0 75
   Temperature Cool 1 4 0 25 Humidity High 3 4 0 75 Wind Strong 2 4 0 5 Step 3 Compute Posterior Probabilities
   Step 4 Prediction Since we predict PlayTennis No Logistic Regression Logistic Regression is a widely used
   supervised machine learning algorithm for binary classification problems predicting two possible outcomes e g
   Yes No 0 1 Despite its name it’s not used for regression in the usual sense the name comes from the fact that
   it predicts probabilities using a logistic function Let’s break it down clearly 1 Idea Behind Logistic
   Regression In linear regression we predict a continuous value But in classification we want to be 0 or 1
   Logistic regression transforms the linear combination into a probability using the sigmoid function also
   called logistic function Where The output is always between 0 and 1 interpretable as a probability Then we
   use a threshold commonly 0 5 to decide the class If If 2 Logistic Regression Equation input features
   coefficients learned from training data 3 How It Works Training Start with random coefficients Use the
   sigmoid function to predict probabilities Compare predictions with actual labels using a loss function Log
   Loss Cross Entropy Loss Optimize coefficients using Gradient Descent to minimize the loss 4
   + 2026 [6529–7763]:
      score Predicted class argmax over C of P C x P X C Under the conditional independence assumption the
      likelihood is calculated as a product P X C P x1 C x P x2 C x x P xn C The evidence P X is the same for
      each candidate class so it can be omitted when comparing class scores 5 Worked Example Weather Prediction
      Suppose we predict whether people will play outside based on Weather and Temperature Weather Temperature
      Play Sunny Mild Yes Sunny Hot No Rainy Mild Yes Rainy Cold No Sunny Mild Yes Rainy Mild No Sunny Mild Yes
      Rainy Cold No New record Weather Sunny Temperature Mild Predict Play Step 1 Calculate prior probabilities
      There are 8 records 4 have Play Yes and 4 have Play No P Yes 4 8 0 5 P No 4 8 0 5 Step 2 Calculate
      likelihoods Among the four Yes records three are Sunny and all four have Mild temperature P Sunny Yes 3 4
      0 75 P Mild Yes 4 4 1 Among the four No records one is Sunny and one has Mild temperature P Sunny No 1 4 0
      25 P Mild No 1 4 0 25 Step 3 Calculate class scores For Play Yes Score Yes 0 5 x 0 75 x 1 0 375 For Play
      No Score No 0 5 x 0 25 x 0 25 0 03125 Step 4 Choose the highest score The Yes score 0 375 is greater than
      the No score 0 03125 so the prediction is Play Yes After normalization the probabilities are approximately
      92 3 for Yes and 7 7 for No The unnormalized scores are sufficient for comparing classes 6 Zero
      Probability and Laplace Smoothing If an attribute value never occurs in a class its estimated likelihood
      is zero Multiplying by zero can make the entire score for that class zero Laplace smoothing adds a small
      count to each possible value For a categorical attribute P xi C N xi C alpha N C alpha x K N xi C is the
      number of records in class C with value xi N C is the total records in class C K is the number of possible
      attribute values alpha is the smoothing parameter commonly 1 7 Types of Naive Bayes Type Suitable data
      Example Gaussian Naive Bayes Continuous numeric attributes Height weight laboratory measurements
      Multinomial Naive Bayes Count data Word counts in documents Bernoulli Naive Bayes Binary attributes
      Whether a word occurs or does not occur Gaussian Naive Bayes assumes numeric attributes follow a Gaussian
      distribution within each class Multinomial Naive Bayes is often used for word frequency counts Bernoulli
      Naive Bayes is useful for binary features 8 Advantages Simple and computationally efficient Works well for
      many high dimensional datasets Requires relatively little training data for some problems Supports
      multiple classes Provides class probability estimates 9 Limitations The conditional independence
      assumption may not hold Zero probabilities can cause problems without smoothing Probability estimates may
      be poorly calibrated Performance may be weaker when attributes are strongly dependent 10 Naive Bayes vs
      Rule Based Classifiers Feature Naive Bayes Rule Based Classifier Main approach Probability calculations IF
      THEN rules Training Estimates prior and likelihood probabilities Learns or receives classification rules
      Prediction Chooses the most probable class Applies matching rules Assumptions Commonly assumes conditional
      independence Depends on rule learning method Interpretability Uses class probabilities Individual rules
      are often easy to explain 11 Student Exercises 16 A dataset contains 100 records 60 belong to Class A and
      40 to Class B Calculate both prior probabilities 17 In Class A 30 out of 60 records have Weather Sunny
      Calculate P Sunny A 18 If P A 0 6 P Sunny A 0 5 and P Mild A 0 8 calculate the Naive Bayes score for Class
      A 19 Explain why Naive Bayes is called naive 20 Explain the purpose of Laplace smoothing Exercise Answers
      21 P A 60 100 0 6 P B 40 100 0 4 22 P Sunny A 30 60 0 5 23 Score A 0 6 x 0 5 x 0 8 0 24 24 It assumes
      attributes are conditionally independent given the class 25 It prevents zero likelihood estimates by
      adding a small count to possible attribute values 12 Summary Naive Bayes is a probabilistic classification
      algorithm based on Bayes theorem It uses prior probabilities and likelihoods to estimate the most probable
      class Essential concepts include prior probability likelihood posterior probability conditional
      independence Laplace smoothing and selecting the class with the highest score The key difference from a
      rule based classifier is that Naive Bayes calculates class probabilities whereas a rule based classifier
      uses IF THEN conditions Logistic Regression Algorithm A Lecture for Machine Learning and Data Mining
      Students Learning Objectives Define Logistic Regression and explain its main purpose Understand the
      sigmoid function and how it converts a linear score into a probability Follow the main steps used to train
      and apply a Logistic Regression model Calculate predicted probabilities and convert them into class labels
      using a decision threshold Understand common evaluation metrics advantages and limitations 1 Introduction
      Logistic Regression is a supervised machine learning algorithm used mainly for classification It estimates
      the probability that an observation belongs to a particular class Although its name contains the word
      regression it is commonly used for classification tasks Examples include predicting whether a student will
      pass or fail whether a customer will leave a service whether an email is spam or whether a medical test
      result is positive or negative 2 Types of Logistic Regression Binary Logistic Regression predicts one of
      two classes such as Yes or No Multinomial Logistic Regression predicts one of three or more unordered
      classes Ordinal Logistic Regression models categories that have a meaningful order such as Low Medium and
      High Specific ordinal models use assumptions that differ from ordinary binary Logistic Regression 3 How
      Logistic Regression Works Logistic Regression first calculates a linear score from the input features It
      then applies the sigmoid function to convert that score into a value between 0 and 1 interpreted as a
      probability The linear score is z b b x b x b x where x x x are input features b is the intercept bias b b
      b are learned model coefficients z is the linear score 4 The Sigmoid Function The sigmoid function is P Y
      1 X 1 1 e The sigmoid function maps any real valued score z to a value strictly between 0 and 1 This
      output can be interpreted as the estimated probability of the positive class For example If z 0 then P Y 1
      X 1 1 e 0 5 If z 2 then P Y 1 X 1 1 0 1353 0 8808 If z 2 then P Y 1 X 1 1 7 389 0 1192 5 Decision
      Threshold and Class Prediction For binary classification a threshold converts the estimated probability
      into a class label A common default is 0 5 although the threshold can be adjusted for the task If P Y 1 X
      0 5 predict Class 1 If P Y 1 X 0 5 predict Class 0 Example if the predicted probability is 0 78 and the
      threshold is 0 5 the predicted class is 1 This does not mean the model is 78 accurate it means the model
      estimates a 78 probability for Class 1 6 Worked Numerical
12. − OLD [4532–4810]:
   based on study hours Hours Studied Pass 1 Fail 0 1 0 2 0 3 0 4 1 5 1 6 1 Fit logistic regression to learn and
   Prediction for 3 5 hours Compute Compute probability of passing If probability 0 5 predict Pass 1 else Fail 0
   5 Advantages Simple and interpretable Outputs probabilities not just classes Works well for binary
   classification 6 Limitations Can’t handle non linear relationships without transformation Assumes linear
   relationship between features and log odds Sensitive to outliers Example Predicting Exam Pass We want to
   predict whether a student passes an exam based on hours studied Hours Studied x Pass y 1 0 2 0 3 0 4 1 5 1 6
   1 Step 1 Logistic Regression Equation We need to learn intercept and slope Step 2 Assume Coefficients For
   simplicity assume after training we got Then Step 3 Predict Probabilities Compute probability of passing for
   each x Hours Studied x z 4 x P y 1 x 1 1 e z 1 3 0 047 2 2 0 119 3 1 0 269 4 0 0 5 5 1 0 731 6 2 0 881 Step 4
   Apply Threshold Threshold 0 5 if P 0 5 predict Pass 1 else Fail 0 Hours Studied x P y 1 x Predicted Class 1 0
   047 0 2 0 119 0 3 0 269 0 4 0 5 1 5 0 731 1 6 0 881 1 Matches the original dataset perfectly Step 5
   Interpretation Probability increases as hours studied increases Logistic regression models the S shaped curve
   sigmoid mapping any value of x to 0 1 Output can be interpreted as probability of success
   + 2026 [7776–8459]:
      Pass 1 Fail 0 based on the number of hours studied For illustration assume a trained Logistic Regression
      model has the following equation z 4 1 2x where x is the number of hours studied The intercept and
      coefficient are assumed to have been learned during training Example A A student studies for 4 hours Step
      1 Calculate the linear score z 4 1 2 4 0 8 Step 2 Apply the sigmoid function P Pass 1 x 4 1 1 e 1 1 0 4493
      0 6900 Step 3 Apply the threshold of 0 5 Because 0 6900 0 5 predict Pass Class 1 Example B A student
      studies for 2 hours z 4 1 2 2 1 6 P Pass 1 x 2 1 1 e 0 1680 Because 0 1680 0 5 predict Fail Class 0 These
      calculations demonstrate prediction after training In a real application the coefficients are estimated
      from labeled training data 7 Main Training Steps 26 Prepare data Collect labeled examples and identify the
      input features and target class 27 Preprocess features Handle missing values and encode categorical inputs
      when necessary Scaling numeric features can help optimization especially when feature magnitudes differ 28
      Split the data Separate training data from validation or test data to evaluate generalization 29
      Initialize the model Set up the Logistic Regression model and its training objective 30 Learn coefficients
      Estimate the intercept and feature coefficients by optimizing the logistic loss commonly binary cross
      entropy often with regularization 31 Estimate probabilities For each new record calculate z and apply the
      sigmoid function 32 Assign a class Compare the probability with a chosen decision threshold 33 Evaluate
      Assess predictions on held out data using appropriate metrics 8 How Are the Coefficients Learned The
      coefficients are not normally chosen by hand The training algorithm adjusts them to make the predicted
      probabilities fit the observed labels For binary classification a common objective is binary cross entropy
      log loss L 1 N y log p 1 y log 1 p Here N is the number of training examples y is the actual label 0 or 1
      and p is the predicted probability for Class 1 Optimization methods such as gradient based methods or
      solver specific methods minimize this loss Regularization may be added to reduce overfitting 9
      Interpreting Coefficients A coefficient describes the change in the log odds of the positive class
      associated with a one unit increase in that feature holding the other features constant The odds ratio for
      a one unit increase is exp b For example if b 0 7 then exp 0 7 2 01 Under the model a one unit increase in
      that feature multiplies the odds of Class 1 by about 2 01 holding other features constant This is an odds
      interpretation not a direct doubling of probability 11 Advantages Simple to implement and relatively fast
      to train Produces probabilities that can support threshold based decisions Coefficients can be interpreted
      through log odds and odds ratios Provides a strong baseline for many binary classification problems Can
      use regularization to help control overfitting 12 Limitations The basic model assumes a linear
      relationship between input features and the log odds of the outcome It may not capture complex nonlinear
      patterns unless features are transformed or interactions are added Performance can be affected by outliers
      multicollinearity poor feature design or data quality A probability estimate is not automatically well
      calibrated calibration should be checked when important The default 0 5 threshold may not be suitable when
      false positives and false negatives have different costs 13 Logistic Regression vs Naive Bayes Aspect
      Logistic Regression Naive Bayes Model type Discriminative models P Y X Generative models P X Y and P Y
      Main approach Learns coefficients by optimizing a loss function Estimates priors and likelihoods from
      training data Feature assumption No conditional independence assumption is required Uses a conditional
      independence assumption in its standard form Output Class probabilities and labels Class probabilities and
      labels Useful when A flexible linear decision boundary and interpretable coefficients are useful Training
      data are limited or conditional feature distributions are reasonably modeled

## Similarity and distance full deduplicated text

**المصادر القديمة:** DM_Similarity_and_Distance (archive).pdf, صفحات فريدة فقط.  **مصادر 2026:** Week 03 - Feature Extraction and Portability.docx, Week4_Feature_Selection.docx, Week8_Clustering.pdf.

**الكلمات المرمّزة:** القديم 3,120؛ الحالي 6,443؛ المتطابق بالترتيب 129. Archive image pages 11–24 duplicate pages 4–10 exactly; use OCR text from the 17 unique image pages plus digital pages 1–3. OCR alignment is provisional; formulas were checked visually.

1. − OLD [1–537]:
   Introduction to Similarity and Distance in Data Mining In data mining the concepts of similarity and distance
   are fundamental for analyzing and comparing data objects Data mining often deals with large volumes of
   heterogeneous data and to discover patterns group objects or classify records we need mathematical measures
   that describe how alike or how different two objects are Distance Dissimilarity measures the degree of
   difference between two objects A smaller distance means objects are closer or more alike while a larger
   distance means they are more different Similarity measures the degree of closeness or resemblance between two
   objects A higher similarity value indicates that objects are more alike These measures are essential in
   Clustering e g K means hierarchical clustering to group similar objects together Classification e g k Nearest
   Neighbors to assign labels based on closeness Information retrieval and text mining e g cosine similarity for
   document comparison Recommender systems e g finding similar users or items Anomaly detection e g identifying
   outliers that are far from others Different types of data numerical categorical text binary mixed type
   require different similarity and distance measures Common measures include Euclidean Manhattan Minkowski
   Chebyshev distances for numeric data and Cosine similarity Jaccard similarity Pearson correlation for vector
   and categorical text data In summary similarity and distance are the backbone of data mining algorithms
   enabling the discovery of meaningful patterns relationships and structures in datasets Why Do We Need
   Similarity and Distance in Data Mining Similarity and distance are core concepts in data mining because they
   provide a way to quantify relationships between data objects Without them algorithms would have no way to
   decide which objects are alike or different Key Reasons 1 Clustering o Distance helps group similar objects
   together o Example In K means clustering objects are assigned to the cluster with the nearest centroid using
   Euclidean distance 2 Classification o Many algorithms e g k Nearest Neighbors classify an object by looking
   at the labels of its closest neighbors o Requires measuring distance to find the nearest neighbors 3 Pattern
   and Relationship Discovery o Similarity measures e g cosine similarity Jaccard index help find objects with
   common patterns o Example Market basket analysis finds items frequently bought together 4 Information
   Retrieval Text Mining o Cosine similarity measures how close two documents are in meaning regardless of size
   o Example Search engines rank documents based on similarity to the query 5 Recommender Systems o Measure
   similarity between users or items to suggest relevant recommendations o Example Netflix recommends movies
   similar to what you’ve already watched 6 Anomaly Detection Outlier Detection o Objects that are far away
   large distance from most others may be anomalies o Example Detecting fraudulent transactions in banking In
   summary We need similarity and distance in data mining because they are the mathematical tools that allow
   algorithms to compare group classify and detect patterns in data Without them tasks like clustering
   classification recommendation and anomaly detection would not be possible Measuring Similarity and Distance
   for Quantitative Data Quantitative data refers to numeric values such as age income height and exam scores To
   compare such objects in data mining we typically compute distance dissimilarity or similarity measures 1
   Euclidean Distance The most common distance measure It
   + 2026 [1–4396]:
      Feature Extraction and Portability Feature extraction Feature extraction is the process of creating new
      features from existing data to represent its important characteristics in a form suitable for data mining
      or machine learning algorithms Obtains useful characteristics from the data Example Suppose we have a
      medical X ray image X ray Image Feature Extraction Texture shape edges intensity Numerical Features
      Classification Instead of giving the complete image directly to a traditional algorithm we can represent
      it using useful features Why Do We Need Feature Extraction Raw data can be very large complex difficult to
      process high dimensional unsuitable for some algorithms Feature extraction can Reduce the amount of data
      Remove unnecessary information Represent important characteristics of the data Make data easier for
      algorithms to process Sometimes improve prediction or classification performance Examples of Feature
      Extraction Different types of data require different extraction methods Data Type Possible Extracted
      Features Image Shape texture edges color Text Word frequency TF IDF embeddings Time Series Mean variance
      frequency components Audio Frequency energy spectral features Spatial Distance density location features
      Sequence Symbol frequencies patterns Graph Degree centrality connectivity Data Type Portability In Data
      Mining data can appear in many different forms Examples Numerical data Age 25 Salary 800 000 Categorical
      data Gender Male Female Text data Medical reports emails reviews Time series data Heart rate recorded
      every second Image data X rays CT scans Spatial data Locations and maps Sequence data DNA sequences Graph
      data Social networks Data Type Portability means converting data from one representation or type into
      another representation so that it can be processed by a data mining algorithm Why Do We Need Data Type
      Portability A dataset may contain several types of information at the same time For example a medical
      dataset may contain age gender medical reports and heart rate measurements Different algorithms are
      designed to work with different forms of data Therefore some data may need to be converted into a suitable
      representation before applying a data mining algorithm Basic process Different Data Types Data Type
      Conversion Suitable Representation Data Mining Algorithm Common Data Type Conversions Numerical
      Categorical Discretization Categorical Numerical Encoding Text Numerical Vectorization Time Series
      Sequence Symbolic representation Time Series Numerical features DFT DWT or feature extraction Image
      Numerical features Feature extraction Graph Numerical representation Graph embedding Any data type Graph
      Similarity graph Numerical Data Categorical Data A common conversion is discretization Discretization
      converts continuous numerical values into a small number of categories or intervals Example 0 17 Young 18
      40 Adult 41 60 Middle aged 61 Older Thus 25 Adult 45 Middle aged 67 Older Advantages Makes numerical data
      easier to understand Can make data suitable for algorithms that require categorical values Disadvantage
      Some information can be lost For example ages 21 and 39 may both become Adult so their exact difference is
      no longer represented Types of Discretization Equal Width Discretization The numerical range is divided
      into intervals of approximately equal numerical size Example Age 0 80 divided into 0 20 21 40 41 60 61 80
      Equal Frequency Discretization Each interval contains approximately the same number of observations
      Example 10 12 15 18 20 30 35 40 Two groups Group 1 10 12 15 18 Group 2 20 30 35 40 Categorical Data
      Numerical Data Many machine learning algorithms require numerical input Suppose the categories are A B O
      One hot encoding creates one binary column for each category Patient P1 A 1 0 0 Patient P2 B 0 1 0 Patient
      P3 O 0 0 1 Here 1 category is present 0 category is absent Why Not Simply Use A 1 B 2 O 3 Using A 1 B 2 O
      3 may incorrectly suggest that the categories have a numerical order For nominal categories such as blood
      type there is no meaningful order Therefore one hot encoding is usually more appropriate for nominal
      categorical data Text Data Numerical Data Text data includes Emails News articles Customer reviews Medical
      reports Social media posts Many numerical algorithms cannot directly process raw text Therefore text is
      converted into numerical features Example Document 1 good product Document 2 good service Vocabulary good
      product service Numerical representation D1 1 1 0 D2 1 0 1 Text Vectorization Common approaches include
      Bag of Words TF IDF Word embeddings Document embeddings General process Text Numerical Representation
      Machine Learning Data Mining The resulting representation may be a numerical vector such as 0 12 0 45 0 08
      0 71 Time Series Numerical Features Sometimes we extract numerical characteristics from a time series
      Example process Original time series Feature extraction Mean standard deviation frequency features wavelet
      features Numerical vector The resulting numerical features can then be used by machine learning algorithms
      Time Series Symbolic Sequence A time series can also be represented using symbols For example Low A Medium
      B High C A numerical series such as 20 22 21 25 27 30 may become A A A B B C The numerical time series has
      been converted into a symbolic sequence Image Data Images are naturally represented using numerical values
      A grayscale image can be represented as a matrix of pixel intensities For example 0 25 80 120 10 40 100
      150 20 60 130 200 For a grayscale image 0 Black 255 White A color RGB image normally contains three
      channels Red Green and Blue Image Numerical Features Instead of using every pixel useful features can be
      extracted Image Feature Extraction Shape Texture Edges Color Deep Features Numerical Vector The numerical
      vector can then be used by a classifier or clustering algorithm Spatial Data Spatial data describes
      objects according to their location Examples GPS coordinates Maps Geographic information Satellite data
      Locations of hospitals Example Hospital H1 Latitude 32 50 Longitude 45 82 Hospital H2 Latitude 32 48
      Longitude 45 85 Spatial information can be transformed into numerical features that data mining algorithms
      can process Sequence Data A sequence is an ordered collection of elements Examples DNA A C G T A C G
      Customer actions Login Search Product Purchase Web navigation Home Products Laptop Checkout The order of
      elements is important Sequence data can sometimes be transformed into numerical features Graph Data A
      graph consists of Nodes vertices Edges connections Example A B C D A B C and D may represent users while
      the edges represent relationships Graph data can be transformed into numerical representations For example
      Node A 0 21 0 75 0 43 Node B 0 19 0 81 0 39 Converting Different Data Types into a Graph Instead of
      converting everything into numerical data relationships between objects can be represented using a graph
      Suppose we have five patients If two patients are sufficiently similar we connect them The nodes represent
      objects and the edges represent similarity Similarity Graph A similarity graph can be created using a
      similarity or distance measure For example If distance P1 P2 threshold Connect P1 and P2 The graph
      represents which objects are similar to each other Applications Clustering Classification Nearest neighbor
      analysis Outlier detection General Data Type Portability Process Different data types can be transformed
      into representations suitable for analysis Numerical Discretization Categorical Encoding Text
      Vectorization Time Series Numerical Features or Symbolic Sequence Image Numerical Features Sequence
      Numerical Features Spatial Numerical Features Graph Numerical Representation The final representation is
      then provided to an appropriate data mining or machine learning algorithm Important Point Conversion Can
      Lose Information Data type conversion is useful but it may result in information loss Example Original
      ages 21 22 39 After discretization Adult Adult Adult The exact ages have disappeared Therefore A good
      conversion should preserve the important information needed for the mining task Advantages of Data Type
      Portability Data Type Portability can 1 Make heterogeneous data easier to process 2 Allow existing
      algorithms to work with different data types 3 Convert complex data into suitable representations 4
      Facilitate integration of different data sources 5 Make machine learning and data mining algorithms easier
      to apply Limitations Data type conversion may have several limitations 1 Information loss 2 Loss of
      original structure 3 Possible distortion of relationships 4 High dimensional representations 5 Additional
      computational cost 6 The converted representation may not be suitable for every algorithm Therefore the
      conversion method should be selected according to the data and the mining task Data Conversion vs Data
      Mining Data Type Portability focuses on How can we represent data in a form suitable for an algorithm Data
      Mining focuses on How can we discover useful patterns or knowledge from the data Therefore Raw Data Data
      Preparation Data Type Conversion Mining Algorithm Patterns Prediction Knowledge Summary Data Type
      Portability is the process of converting data from one representation to another so that it can be
      processed by data mining algorithms Important examples Numerical Categorical Discretization Categorical
      Numerical One hot encoding Text Numerical TF IDF embeddings Time Series Numerical Feature extraction Time
      Series Sequence Symbolic representation Image Numerical Feature extraction Sequence Numerical Sequence
      encoding Graph Numerical Graph embedding Main idea Different data types require different representations
      Data Type Portability allows us to transform data into a representation that is more suitable for analysis
      and mining Quick Reference Table From To Example Technique Numerical Categorical Discretization
      Categorical Numerical One hot encoding Text Numerical TF IDF embeddings Time Series Numerical Feature
      extraction Time Series Sequence Symbolic representation Image Numerical Feature extraction Sequence
      Numerical Sequence encoding Graph Numerical Graph embedding Feature Selection Techniques in Data Mining
      Feature selection is the process of selecting the most relevant features attributes from a dataset while
      removing irrelevant or redundant features For example if we want to predict whether a patient has diabetes
      the dataset may contain Age Glucose BMI Blood Pressure Insulin Skin Thickness Pregnancies Patient ID Some
      features may contribute strongly to prediction while others may provide little or no useful information
      Feature selection attempts to keep the useful features and remove the unnecessary ones Why is Feature
      Selection Important Feature selection can Reduce the number of features Remove irrelevant and redundant
      features Reduce computational cost Improve model performance in some cases Reduce the risk of overfitting
      Make the model easier to interpret Help visualize high dimensional data Main Feature Selection Techniques
      Feature selection techniques are commonly divided into three main categories Filter Methods Wrapper
      Methods Embedded Methods A simple way to remember them is Filter evaluate features Wrapper evaluate
      feature subsets using a model Embedded select features during model training 1 Filter Methods Filter
      methods select features based on their statistical characteristics without using a data mining algorithm
      to evaluate the final feature subset They are usually fast and suitable for datasets with many features
      Common Filter Techniques 1 1 Correlation Correlation measures the relationship between two variables For
      example Feature Correlation with Target Glucose 0 47 BMI 0 29 Age 0 24 Patient ID 0 01 Features with very
      weak relationships with the target may be removed Example If the correlation between Patient ID and
      diabetes is approximately 0 Patient ID is probably not useful for prediction Important Low correlation
      does not always mean that a feature is useless because correlation mainly captures certain types of
      relationships especially linear relationships How to Calculate Correlation In data mining correlation
      measures the strength and direction of the relationship between two numerical variables The most commonly
      used measure is Pearson correlation coefficient denoted by 1 Pearson Correlation Formula Where value of
      variable value of variable mean of mean of number of observations correlation coefficient 2 Simple Example
      Suppose we have Age and Blood Pressure for five people Person Age X Blood Pressure Y 1 20 110 2 30 120 3
      40 130 4 50 140 5 60 150 Step 1 Calculate the means Step 2 Calculate deviations X Y 20 110 20 20 30 120 10
      10 40 130 0 0 50 140 10 10 60 150 20 20 Step 3 Calculate the products Therefore Step 4 Calculate squared
      deviations Similarly Step 5 Calculate So the correlation is This means there is a perfect positive linear
      correlation between Age and Blood Pressure in this example 1 2 Chi Square Test The Chi square test
      measures the relationship between categorical features and a categorical target For example Smoking Status
      Heart Disease A high Chi square statistic indicates a stronger association between the feature and the
      target It is commonly used for classification problems with categorical or non negative discrete features
      Example Suppose we want to predict whether a person has Heart Disease based on Smoking Status We have
      Heart Disease Yes Heart Disease No Total Smoker 40 20 60 Non Smoker 20 70 90 Total 60 90 150 The Chi
      Square test compares Observed frequencies what we actually see in the dataset Expected frequencies what we
      would expect if Smoking Status and Heart Disease were independent Hypotheses The Chi Square test uses two
      hypotheses Null hypothesis The feature and the target are independent In our example Smoking Status is not
      associated with Heart Disease Alternative hypothesis The feature and the target are associated In our
      example Smoking Status is associated with Heart Disease Calculate Expected Frequencies The expected
      frequency is calculated as For Smoker Heart Disease Yes For Smoker Heart Disease No For Non Smoker Heart
      Disease Yes For Non Smoker Heart Disease No Therefore Disease Yes Disease No Smoker Observed 40 Observed
      20 Expected 24 Expected 36 Non Smoker Observed 20 Observed 70 Expected 36 Expected 54 Calculate Chi Square
      Statistic The formula is where Observed frequency Expected frequency For our example Therefore A
      relatively large Chi Square value indicates that the observed frequencies differ substantially from what
      would be expected if the variables were independent What Does the Chi Square Value Mean A larger Chi
      Square statistic generally indicates stronger evidence of an association between the feature and target
      However when using Chi Square for feature selection it is often more convenient to look at the p value For
      a table Therefore We then use the Chi Square distribution to obtain the p value If we commonly reject and
      conclude that there is statistical evidence of an association between the feature and target 1 3
      Information Gain Information Gain measures how much information a feature provides about the target A
      feature that significantly reduces uncertainty about the target has high information gain For example
      Feature A Information Gain 0 42 Feature B Information Gain 0 08 Feature A would generally be considered
      more informative than Feature B Information Gain is commonly associated with decision tree based feature
      selection Information Gain for Feature Selection Simple Example Suppose we want to predict whether a
      student will Pass or Fail We have 8 students Student Attendance Study Hours Result 1 High High Pass 2 High
      High Pass 3 High Low Pass 4 High Low Fail 5 Low High Pass 6 Low Low Fail 7 Low Low Fail 8 Low High Fail We
      want to answer Which feature is more useful for predicting the Result Attendance or Study Hours Step 1
      Calculate the initial Entropy There are Pass 4 Fail 4 Therefore So Step 2 Calculate Information Gain for
      Attendance Attendance has two groups High Attendance Students 1 4 Result Number Pass 3 Fail 1 Entropy Low
      Attendance Students 5 8 Result Number Pass 1 Fail 3 Therefore Weighted Entropy Each group contains 4 out
      of 8 students Information Gain Step 3 Calculate Information Gain for Study Hours High Study Hours Students
      1 2 5 8 Result Number Pass 3 Fail 1 Therefore Low Study Hours Students 3 4 6 7 Result Number Pass 1 Fail 3
      Therefore Weighted Entropy Information Gain Step 4 Compare Them Feature Information Gain Attendance 0 189
      Study Hours 0 189 In this particular dataset both features have the same Information Gain Therefore based
      only on Information Gain Attendance and Study Hours provide the same amount of information about the
      student's result The basic process to teach students Attendance Information Gain 0 189 Compare Study Hours
      Information Gain 0 189 The general rule is So if Attendance had an Information Gain of 0 35 and Study
      Hours had 0 12 we would select Attendance as the more informative feature 1 4 Mutual Information Mutual
      Information MI measures the amount of information shared between a feature and the target It can capture
      nonlinear relationships which makes it different from simple correlation For example If Feature X has a
      nonlinear relationship with the target correlation might be low while mutual information may still be high
      The main equation for Mutual Information MI is Where the feature the target uncertainty entropy of the
      target before knowing the feature uncertainty of the target after knowing the feature Information Gain How
      much does the feature reduce the uncertainty of the target Mutual Information How much information does
      the feature and target share Example Suppose we want to predict whether a student will Pass or Fail We
      have two features Attendance Study Hours Dataset Student Attendance Study Hours Result 1 High High Pass 2
      High Low Pass 3 High High Pass 4 High Low Pass 5 Low High Fail 6 Low Low Fail 7 Low Low Fail 8 Low High
      Fail Notice that Attendance perfectly separates the two classes High Pass Low Fail But Study Hours does
      not High sometimes Pass sometimes Fail Low sometimes Pass sometimes Fail 1 Mutual Information of
      Attendance Before using Attendance Pass 4 Fail 4 Therefore After knowing Attendance Attendance High All 4
      students Pass Attendance Low All 4 students Fail Therefore So 2 Mutual Information of Study Hours Now
      consider Study Hours Study Hours High Students Student Result 1 Pass 3 Pass 5 Fail 8 Fail So Pass 2 Fail 2
      Therefore Study Hours Low Students Student Result 2 Pass 4 Pass 6 Fail 7 Fail Again Pass 2 Fail 2
      Therefore Thus and 3 Compare the Two Features Feature Mutual Information Attendance 1 0 Study Hours 0 0
      Therefore Why Attendance completely determines the result in this example High attendance Pass Low
      attendance Fail But Study Hours provides no useful information here because both High and Low study hours
      contain an equal number of Pass and Fail students 1 5 Variance Threshold This method removes features with
      very low variance If a feature has almost the same value for every observation it provides little
      information for distinguishing observations Example Patient Feature 1 1 2 1 3 1 4 1 5 1 This feature has
      zero variance and can usually be removed 2 Wrapper Methods Wrapper methods use a data mining or machine
      learning algorithm to evaluate different subsets of features Instead of evaluating features individually
      they ask Which combination of features produces the best model performance Common Wrapper Techniques 2 1
      Forward Selection Starts with no features Then Add the feature that improves performance the most Add
      another feature that provides the next largest improvement Continue until a stopping condition is reached
      Example Start No features Add Glucose Add BMI Add Age Add Blood Pressure Final subset 2 2 Backward
      Elimination Starts with all features Then Train the model using all features Remove the least useful
      feature Retrain the model Continue removing features Example All features Remove Patient ID Remove Skin
      Thickness Remove Insulin Final subset 2 3 Recursive Feature Elimination RFE RFE repeatedly trains a model
      and removes the least important features For example 10 features Train model Remove least important
      feature 9 features Train model Remove least important feature 5 selected features RFE can be used with
      algorithms such as Logistic Regression SVM and Random Forest depending on the implementation 3 Embedded
      Methods Embedded methods perform feature selection during the model training process Therefore feature
      selection is part of the learning algorithm itself Common Embedded Techniques 3 1 LASSO Regression LASSO
      uses L1 regularization It adds a penalty to the model The L1 penalty can force some coefficients to become
      exactly zero For example Feature Coefficient Glucose 0 82 BMI 0 31 Age 0 15 Insulin 0 Patient ID 0
      Features with coefficients equal to zero can be removed 3 2 Decision Trees Decision trees select features
      when constructing the tree For example Glucose High Low BMI Age The tree gives greater importance to
      features that provide useful splits Feature importance can then be used for feature selection 3 3 Random
      Forest Feature Importance Random Forest can calculate feature importance based on how much features
      contribute to reducing impurity or depending on the method how much they affect prediction performance
      Example Feature Importance Glucose 0 31 BMI 0 18 Age 0 14 Blood Pressure 0 09 Patient ID 0 00 Features
      with very low importance may be removed Comparison of the Three Main Methods Method Basic Idea Model
      Required Speed Filter Evaluate features using statistical measures No Fast Wrapper Evaluate feature
      subsets using a model Yes Slow Embedded Select features during model training Yes Medium Fast Simple
      Example Suppose we have 20 features and want to select the most useful ones Filter Calculate statistical
      scores select top 8 features Wrapper Try different combinations train model choose the subset producing
      the best performance Embedded Train a model model automatically assigns zeros feature coefficients or
      importance select important features Key Difference Filter methods select features before model training
      Wrapper methods select features by repeatedly evaluating a model Embedded methods select features as part
      of model training DATA MINING WEEK 8 Week 8 Clustering WEEK 8 CLUSTERING Clustering as an Application of
      Data Mining 1 Introduction to Data Mining Data Mining is the process of discovering useful patterns
      relationships trends and knowledge from large amounts of data It uses techniques from statistics machine
      learning databases and artificial intelligence to analyze data and support decision making The main
      purpose of Data Mining is not simply to store or retrieve data Its purpose is to discover information that
      may not be immediately obvious from the original data 1 1 Example of Data Mining A university may collect
      information about students such as attendance study hours assignment marks and examination results Data
      Mining techniques can analyze these records to discover patterns identify students who may need support or
      group students with similar academic behavior 1 2 Main Tasks of Data Mining Data Mining Task Purpose
      Example Classification Assign an item to one of several predefined categories Classify an email as spam or
      not spam Prediction Regression Estimate a numerical value or a future outcome Predict a student's final
      mark Clustering Group similar data items without predefined class labels Group students according to
      academic behavior Association Rule Mining Discover items or events that frequently occur together Find
      products commonly purchased together Anomaly Detection Identify unusual patterns or observations Detect
      unusual banking transactions Summarization Provide a compact description of a dataset Summarize customer
      characteristics Remember Classification asks Which known category does this record belong to Clustering
      asks Which records are similar to one another 2 Supervised and Unsupervised Learning Machine learning
      methods are commonly divided into supervised learning and unsupervised learning according to whether the
      training data contain known target labels Aspect Supervised Learning Unsupervised Learning Training data
      Contains input features and known labels Contains input features without target labels Main purpose Learn
      to predict a known target Discover hidden structures or patterns Typical tasks Classification and
      regression Clustering and dimensionality reduction Example Predict whether a transaction is fraudulent
      using labeled examples Group transactions with similar behavior without labels DATA MINING WEEK 8 Week 8
      Clustering For example if student records already contain labels such as Excellent Good and Needs Support
      a model can learn to predict those labels This is supervised learning If labels are not provided and an
      algorithm discovers groups of similar students this is unsupervised learning 3 Clustering as an
      Application of Data Mining Clustering is an important Data Mining task It divides a dataset into groups
      called clusters so that data objects in the same group are more similar to one another than to objects in
      other groups Unlike classification clustering does not require predefined class labels The algorithm
      examines the data and attempts to discover groups based on similarities or distances between objects 3 1
      University Example Suppose a university has records for 500 students Each record contains attendance
      percentage weekly study hours assignment score and examination score The university does not provide
      predefined student categories A clustering algorithm may discover groups such as Cluster 1 students with
      high attendance high study hours and high marks Cluster 2 students with moderate attendance and moderate
      marks Cluster 3 students with low attendance and low marks These group descriptions are interpretations
      made after examining the clusters The algorithm itself discovers groups from the data it does not
      automatically know the educational meaning of each group 3 2 Relationship Between Data Mining Machine
      Learning and Clustering Concept Meaning Data Mining A broader process of discovering useful patterns and
      knowledge from data Machine Learning A set of computational methods that learn patterns from data
      Unsupervised Learning A machine learning approach that works with data without target labels Clustering A
      common unsupervised learning task used to group similar data objects K Means DBSCAN Hierarchical
      Algorithms that perform clustering in different ways Therefore clustering is a Data Mining task and is
      commonly performed using unsupervised learning algorithms Data Mining and Machine Learning are related but
      they are not identical terms 4 Introduction to Clustering Clustering is the process of organizing a
      collection of data objects into groups based on their similarity Each group is called a cluster Objects in
      the same cluster should be relatively similar while objects in different clusters should be relatively
      dissimilar 4 1 Main Objectives of Clustering Discover natural groups or structures in data Understand the
      characteristics of different groups Summarize large datasets using a smaller number of groups Identify
      unusual objects that do not fit well into any group Support further analysis and decision making 4 2
      Applications of Clustering Application Area Example Marketing Group customers according to purchasing
      behavior Healthcare Group patients according to similar clinical measurements DATA MINING WEEK 8 Week 8
      Clustering Education Group students according to learning or academic patterns Image Analysis Group pixels
      or image regions with similar properties Cybersecurity Group network activities and investigate unusual
      groups Document Analysis Group scientific papers according to their content 5 Similarity and Distance
      Measures Clustering algorithms need a way to compare data objects A distance measure indicates how far
      apart two objects are A similarity measure indicates how alike they are The appropriate measure depends on
      the type of data and the clustering algorithm 5 1 Euclidean Distance Euclidean distance
2. − OLD [546–1794]:
   in multi dimensional space Used in clustering k means k NN classification 2 Manhattan Distance City Block or
   L1 Norm Measures distance as the sum of absolute differences Useful when movement is restricted to grid like
   paths 3 Minkowski Distance Generalized Form A generalized distance metric 4 Chebyshev Distance L Norm Takes
   the maximum absolute difference between coordinates Useful in chess king’s move distance or tolerance based
   systems 5 Cosine Similarity Angle based Measure Measures similarity based on the angle between two vectors
   not magnitude Example Used in text mining to compare documents 6 Pearson Correlation Coefficient Measures the
   linear relationship between two numeric variables High positive strong similarity High negative strong
   dissimilarity Summary Table Measure Formula Idea Best Use Case Euclidean Distance Straight line distance
   Clustering k NN Manhattan Distance Absolute differences Sparse data grid movement Minkowski Distance
   Generalized Lp norm Flexible distance choice Chebyshev Distance Max difference Chess moves tolerance checks
   Cosine Similarity Angle between vectors Text mining high dimensional data Pearson Correlation Linear
   relationship Pattern detection statistics Common Distance Similarity Measures 1 Euclidean Distance L2 Norm
   Formula n d x y xi yi 2 Intuition Straight line distance in n dimensional space Example Distance between 3 4
   and 7 1 3 7 2 4 1 2 16 9 25 5 Used in K means clustering k NN classification 2 Manhattan Distance City Block
   L1 Norm Formula d x y lxi yil 1 Intuition Distance if you can only move in grid like up down sideways steps
   Example 3 4 and 7 1 3 7 4 1 4 3 7 Used in Grid pathfinding clustering with high dimensional data 3 Minkowski
   Distance Generalized Lp Norm Formula d x y lxi yilP 1 Special cases p 1 Manhattan p 2 Euclidean p oo
   Chebyshev Used in Generalized distance metric for flexible similarity calculations 4 Chebyshev Distance Loo
   Norm Maximum Distance Formula d x y max Ix yil Intuition The largest coordinate difference Example 3 4 and 7
   1 max 13 7l 14 11 max 4 3 4 Used in Chess king's move Chebyshev distance tolerance based systems 5 Cosine
   Similarity Angle based Formula x y xiyi sim x y IIxIl lyl Vx y Range 1 1 but usually 0 1 for non negative
   vectors Intuition Compares direction angle between two vectors ignoring magnitude Example Common in text
   mining recommender systems If vectors are identical similarity 1 If vectors are orthogonal similarity 0 If
   vectors are opposite similarity 1 Quick Use Cases Euclidean Best for geometric continuous space Manhattan
   Best for grid or sparse high dimensional data Minkowski Generalization tweak p as needed Chebyshev When
   maximum deviation matters Cosine similarity When angle orientation matters more than magnitude e g text user
   preferences Pearson Correlation Coefficient Formula 10 x x xi x vi y 2 Where Xi Y individual data points x y
   means of X and Y r 1 1 Example Hours Studied vs Exam Score Person Hours Studied X Exam Score Y A 2 50 B 60 6
   65 D 8 80 E 10 85 Step1 CalculateMeans 2 4 6 8 10 5 50 60 65 80 85 68 5 Step 2 Compute Numerator Person x yi
   Xi x yi y Product A 2 50 4 18 72 B 60 2 8 16 6 65 0 3 0 Person xi x yi y Product D 8 80 2 12 24 E 10 85 17 68
   Sum 180 x x v y 180 Step 3 Compute Denominator For X 4 2 02 22 42 40 For Y 18 8 3 12 17 830 So denominator 40
   830 33200 182 2 Step 4 Final Calculation 180 0 99 182 2 Result r 0 99 very strong positive linear
   relationship This means the more hours a person studies the higher their exam score Minkowski Distance
   Formula d x y lxi yilP 1 If p 1 Manhattan distance If p 2 Euclidean distance If p oo Chebyshev distance
   Example Points A 3 4 and B 7 1 Step 1 Differences in each coordinate 3 7 4 14 1 3 So differences 4 3 Step 2
   Plug into formula with different p values Case 1 p 1 Manhattan d 1411 311 1 1 4 3 7 Case 2 p 2 Euclidean d
   1412 1312 1 2 16 9 1 2 25 5 Case 3 p 3 d 1413 1313 1 3 64 27 1 3 911 3 4 497 Case 4 p 0o Chebyshev d max l4l
   I31 4 Summary of Distances between 3 4 and 7 1 p 1 7 Manhattan p 2 5 Euclidean p 3 4 50 p o0 4 Chebyshev
   Cosine Similarity Formula K1x x y sim x y Ilxlllyll Range 1 1 1 exactly the same direction most similar 0
   vectors are orthogonal no similarity 1 exactly opposite directions Example Let's compare two vectors x 1 2 3
   y 4 5 6 Step 1 Compute the dot product 7 81 01 9 s z 1 x Step 2 Compute magnitudes llxll 12 22 32 1 4 9 14 3
   742 Ilyll 42 52 62 16 25 36 77 8 775 Step 3 Plug into formula 32 32 sim x y 0 9746 3 742 8 775 32 87 Result
   Cosine Similarity x y 0 975 This means the vectors are very similar in direction almost pointing the same way
   In practice Text Mining TF IDF vectors Compare similarity between documents Recommender Systems Compare users
   items based on preference vectors Measuring Similarity and Distance for Categorical Data Categorical data
   includes nominal attributes like color gender or product type or ordinal attributes like ratings low medium
   high Standard numerical distance measures like Euclidean cannot be applied directly Instead we use
   specialized techniques 1 Simple Matching Coefficient SMC Measures similarity based on matches and mismatches
   between categorical values Formula Number of matches SMC x y Total number of attributes Distance d x y 1 SMC
   x y Example x red small circle y red large circle Matches 2 red circle Total 3 SMC 2 3 0 667 d 0 333 Jaccard
   Coefficient for binary categorical attributes Ignores attributes that are absent in both objects Useful for
   sparse data Formula lx yl Jaccard x y lx Uyl Example items purchased by customers x milk bread y bread butter
   Intersection 1 bread Union 3 milk bread butter Jaccard 1 3 0 333 Hamming Distance Counts the number of
   attribute positions where two objects differ Formula 0 if xi yi d x y 8 xi yi 8 xi yi ifxi yi 1 Example x red
   small circle y red large square Differences 2 small large circle square so d 2 Goodall's Measure Weighted
   Matching Assigns higher weight to matches on rare attribute values Useful when some categorical values are
   very common and less informative Overlap Metric for Mixed Data Combines numeric and categorical attributes
   into a single similarity distance measure Categorical part uses matching 0 or 1 numeric part uses normalized
   difference Key Points For categorical data matching based measures Simple Matching Hamming Jaccard are most
   common Choice depends on Binary vs multi valued attributes Importance of rare categories Whether to ignore
   simultaneous absence Jaccard does SMC doesn't These measures are widely used in clustering categorical data k
   modes k prototypes similarity search and recommender systems Text Similarity Measures Text similarity
   measures are used to compare documents sentences or words based on content structure or meaning They are
   widely used in information retrieval document clustering plagiarism detection and recommender systems 1
   Cosine Similarity Definition
   + 2026 [4405–4510]:
      For two points A x y and B x y the formula is d A B x x y y Example Let A 2 3 and B 5 7 d A B 5 2 7 3 3 4
      9 16 25 5 The Euclidean distance between A and B is 5 A smaller distance means the points are closer 5 2
      Manhattan Distance Manhattan distance is the sum of the absolute differences between corresponding
      coordinates d A B x x y y Using A 2 3 and B 5 7 d A B 5 2 7 3 3 4 7 5 3 Cosine Similarity Cosine
      Similarity
3. − OLD [1801–3120]:
   in a multi dimensional space ignoring magnitude Formula x y xiyi sim x y Ixl lyl Vx y Example Compare two TF
   IDF vectors of documents Use Case Document clustering search ranking plagiarism detection Jaccard Similarity
   Set Based Definition Measures overlap between sets of words or n grams in two texts Formula A N BI sim A B A
   U BI Example A data mining techniques B data analysis techniques A B 2 A U B 4 sim 0 5 Use Case Plagiarism
   detection text deduplication Edit Distance Levenshtein Distance Definition Counts the minimum number of edits
   insertions deletions substitutions needed to transform one string into another Formula Algorithmic dynamic
   programming Example kitten sitting 3 edits substitute k s e i append g Use Case Spell correction fuzzy
   matching DNA sequence comparison Dice Coefficient Definition Similar to Jaccard gives weight to common terms
   Formula 2 A N BI sim A B A B Example Using the same word sets as Jaccard above 2 2 Sim 4 0 667 3 3 Use Case
   Information retrieval document similarity NLP tasks TF IDF with Cosine Similarity Definition Represents
   documents as weighted vectors using term frequency TF and inverse document frequency IDF then computes cosine
   similarity Use Case Ranking search results document clustering content based recommendation Word Embedding
   Similarity Semantic Definition Uses word or sentence embeddings Word2Vec GloVe BERT to capture meaning
   Similarity Typically cosine similarity between embedding vectors Use Case Semantic search question answering
   systems chatbots Key Insights Bag of Words Set Based Measures Jaccard Dice Focus on common words ignore order
   Vector Based Measures Cosine with TF IDF or embeddings Consider frequency and importance of terms Edit
   Distance Works on character level differences useful for spelling fuzzy matching Embedding Similarity
   Captures semantic meaning not just exact words Temporal Similarity Measures Temporal or time based similarity
   measures are used in data mining time series analysis and sequence mining to quantify how similar two
   sequences or time dependent datasets are These measures consider both the values and the order timing of
   events Euclidean Distancefor TimeSeries Definition Measures the straight line distance between corresponding
   points in two sequences Formula n d X Y X Y 2 Example X 2 4 6 Y 3 5 7 d 2 3 2 4 5 2 6 7 2 3 1 732 Limitation
   Sensitive to shifts in time sequences must be aligned Dynamic Time Warping DTW Definition Measures similarity
   by warping the time axis allowing sequences to match even if they are stretched or shifted in time Algorithm
   Finds the optimal alignment minimal cumulative distance between sequences Example Matching two walking
   patterns or speech signals with different speeds Use Case Time series clustering gesture recognition speech
   recognition Longest Common Subsequence LcsS Definition Measures similarity based on the length of the longest
   common subsequence between sequences Formula Length of LCS similarity X Y min IXI IYI Example X A B C D Y A C
   D E Longest common subsequence A C D similarity 3 4 0 75 Use Case Sequence mining trajectory similarity DNA
   protein sequence comparison Edit Distance on Sequences Levenshtein Distance Definition Measures the minimum
   number of edits insertions deletions substitutions to transform one sequence into another Example X A B C Y A
   C D Edits 2 delete B insert D distance 2 Use Case Time series comparison event sequence matching 5Correlation
   Based Similarity Definition Measureshowtwotimeseriesco varyovertime Formula Pearson correlation coefficient
   between sequences Example Two stock price series moving together Use Case Financial time series sensor data
   analysis Key Insights Temporal similarity is not just about values but also about ordering and timing Direct
   distance measures Euclidean Good for aligned series Warping sequence based measures DTW LCSS Edit Distance
   Good for sequences with temporal shifts Correlation based measures Focus on trend similarity ignoring
   absolute values Graph Similarity Measures Graphs are structures composed of nodes vertices and edges
   representing relationships in social networks biological networks chemical compounds and many other domains
   Graph similarity measures quantify how similar two graphs or subgraphs are 1 Graph Isomorphism Definition Two
   graphs are isomorphic if there exists a one to one mapping of nodes that preserves adjacency Similarity
   Measure 1 if G G2 sim G1 G2 O otherwise Use Case Checking structural equivalence chemical compound matching 2
   Graph Edit Distance GED Definition Minimum number of graph edit operations node edge insertion deletion
   substitution required to transform one graph into another Formula text GED G 1 G 2 min text of edits to
   convert G 1 text to G 2 Example G1 has 4 nodes and 3 edges G2 has 4 nodes and 4 edges GED 1 add one edge Use
   Case Chemical structure similarity pattern recognition Maximum Common Subgraph MCS Definition Measures
   similarity based on the largest common subgraph between two graphs Formula IVmcsl Emcsl sim G1 G2 IVl V2l E
   E2l Use Case Molecular similarity detecting common patterns in networks Graph Spectral Similarity Definition
   Compares eigenvalues or eigenvectors of graph adjacency or Laplacian matrices Similarity Measure 1 2ll sim G1
   G2 1 max ll Il II2Il where l1 l2 are eigenvalue vectors of G1 and G2 Use Case Graph classification network
   motif detection Node Edge Attribute Similarity Definition If nodes edges have attributes labels weights
   similarity can be computed using vector based measures e g cosine similarity Euclidean distance on attributes
   then aggregated Example Compare social network graphs based on node degrees or centrality measures Use Case
   Attributed network comparison labeled graph mining Graph Kernel Methods Definition Map graphs into a high
   dimensional space to compute inner products capturing similarity without explicit subgraph enumeration
   Examples Random walk kernel shortest path kernel Weisfeiler Lehman kernel Use Case Machine learning on graphs
   graph classification tasks Key Insights Graph similarity depends on structure attributes and labels Exact
   measures Isomorphism MCS strict match Approximate measures GED spectral similarity graph kernels allow
   partial similarity Use Cases Social network analysis chemical molecular similarity fraud detection
   bioinformatics Supervised Similarity Functions In supervised learning similarity functions are used to
   measure how similar data points are while considering class labels Unlike unsupervised similarity supervised
   similarity leverages label information to improve classification clustering or regression tasks Definition A
   supervised similarity function is a function S xi x 0 1 or R where Xi Xj are feature vectors of two objects S
   xi x is higher for objects in the same class and lower for objects in different classes Key Approaches a
   Label Weighted Similarity Idea Assign higher similarity if two objects share the same class Formula example
   sim xi xj if y yj S xi xj 0 ifyiy Use Case k NN with class based weighting supervised clustering b
   Mahalanobis Distance Based Similarity Idea Learns a distance metric that maximizes similarity within classes
   and minimizes similarity between classes Distance formula dM xi xj xi xj TM xi xj M is a learned positive
   semi definite matrix using labeled data Similarity function S xi xj 1 dM xi x Use Case Metric learning
   supervised k NN face recognition c Supervised Kernel Functions Idea Use class labels to construct kernels
   that map data into a higher dimensional space where same class objects are closer Example Supervised RBF
   kernel IIx x l12 K xi xj exp 1y yj 2g2 Use Case Support Vector Machines SVMs kernel based supervised learning
   d Class Based Cosine Similarity Compute cosine similarity between feature vectors only for same class objects
   x x S xi xj ifyi yj Encourageshigh similarity within classes low similarity across classes Key Applications
   Supervised Clustering Improves cluster quality using labels Metric Learning Learns distances that respect
   class labels e g k NN Mahalanobis metric Classification Weighted k NN kernel based classifiers Recommendation
   Systems Incorporates user item labels to refine similarity Key Insights Supervised similarity functions
   leverage label information to make similarity more meaningful for learning tasks They are widely used in
   metric learning supervised clustering and kernel based supervised algorithms Choosing the right function
   often depends on data type feature space and available labels
   + 2026 [4517–6443]:
      It is often useful for text data because it compares vector direction rather than their absolute
      magnitudes Cosine Similarity A B A B A B Its common range is from 1 to 1 For non negative text vectors
      values are usually between 0 and 1 A value closer to 1 indicates greater similarity Important Features
      measured on very different scales can dominate distance calculations For methods based on distance
      consider normalizing or standardizing numerical features 5 4 Worked Example Cosine Similarity in Document
      Clustering Suppose we have three documents and want to group them according to their content A text
      vectorization method converts each document into a numerical vector For this simplified example assume the
      following Document Content Vector A Data Mining and AI 1 1 0 B Data Mining and Machine Learning 1 1 1 C
      Football and Sports 0 0 2 DATA MINING WEEK 8 Week 8 Clustering Step 1 Calculate the similarity between
      Documents A and B First calculate the dot product A B 1 1 1 1 0 1 2 Next calculate the magnitude length of
      each vector A 1 1 0 2 B 1 1 1 3 Substitute these values into the Cosine Similarity formula Cosine A B 2 2
      3 2 2 449 0 816 Interpretation Documents A and B have relatively high similarity because their vectors
      point in similar directions Step 2 Calculate the similarity between Documents A and C Calculate the dot
      product A C 1 0 1 0 0 2 0 Calculate the magnitudes A 2 C 0 0 2 2 Apply the formula Cosine A C 0 2 2 0
      Interpretation Documents A and C have no directional similarity in this simplified example Step 3 Compare
      the similarity values Document Pair Cosine Similarity Interpretation A and B 0 816 Relatively high
      similarity A and C 0 000 No directional similarity Step 4 Form possible clusters Based on the similarity
      values Documents A and B are more similar to each other while Document C is different from them A possible
      grouping is Cluster Documents Description Cluster 1 A and B Technology related documents Cluster 2 C
      Sports related document The cluster descriptions are assigned by a person after examining the documents
      The similarity calculation compares the numerical representations it does not automatically assign
      meaningful labels Converting Cosine Similarity into Cosine Distance Some clustering methods use a distance
      value rather than a similarity value A simple cosine distance is DATA MINING WEEK 8 Week 8 Clustering
      Cosine Distance 1 Cosine Similarity For Documents A and B Cosine Distance A B 1 0 816 0 184 A smaller
      cosine distance indicates greater similarity Cosine Similarity is a similarity measure not a clustering
      algorithm It can be used with suitable clustering methods such as hierarchical clustering 6 Main Types of
      Clustering Algorithms Clustering algorithms use different strategies to form groups This lecture
      introduces four common families partitioning hierarchical density based and model based clustering 6 1
      Partitioning Clustering K Means K Means is a partitioning algorithm that divides a dataset into K clusters
      Each cluster is represented by its centroid which is the mean position of the objects assigned to that
      cluster How K Means Works 1 Choose the number of clusters K 2 Initialize K centroids The initial centroids
      may be selected randomly or using K Means 3 Calculate the distance from each data object to each centroid
      4 Assign each object to the cluster with the nearest centroid 5 Recalculate each centroid as the mean of
      the objects assigned to its cluster 6 Repeat the assignment and centroid update steps until the
      assignments or centroids stop changing significantly Simple Example Suppose the one dimensional data
      values are 2 4 10 and 12 and K 2 If the initial centroids are 2 and 10 the nearest centroid assignments
      are Data Point Distance to Centroid 2 Distance to Centroid 10 Assigned Cluster 2 0 8 Cluster 1 4 2 6
      Cluster 1 10 8 0 Cluster 2 12 10 2 Cluster 2 The new centroid of Cluster 1 is 2 4 2 3 The new centroid of
      Cluster 2 is 10 12 2 11 The algorithm repeats the process using these updated centroids Advantages of K
      Means Simple to understand and implement Efficient for many numerical datasets Works well when clusters
      are compact and reasonably separated Limitations of K Means The value of K must be selected in advance
      Results can depend on the initial centroids It is sensitive to outliers and feature scaling It may perform
      poorly when clusters have irregular shapes or very different densities DATA MINING WEEK 8 Week 8
      Clustering K Means Initialization K Means is an initialization method designed to choose starting
      centroids that are spread out It generally reduces the chance of selecting poor initial centroids It does
      not change the basic assignment and centroid update steps of K Means 6 2 Hierarchical Clustering
      Hierarchical clustering creates a hierarchy of clusters Its result is commonly represented using a tree
      like diagram called a dendrogram Two Main Approaches Approach Description Agglomerative bottom up Starts
      with each object as its own cluster and repeatedly merges the closest clusters Divisive top down Starts
      with all objects in one cluster and repeatedly splits clusters into smaller groups Linkage Methods When
      two clusters contain multiple objects a linkage method defines how the distance between the clusters is
      calculated Linkage Method How Cluster Distance Is Calculated Single linkage Minimum distance between any
      pair of objects one from each cluster Complete linkage Maximum distance between any pair of objects one
      from each cluster Average linkage Average of the distances between all cross cluster object pairs Ward's
      method Merges clusters to minimize the increase in within cluster variance Dendrogram A dendrogram
      displays the sequence of merges or splits and the distances at which they occur To obtain a chosen number
      of clusters a horizontal cut can be made across the dendrogram The number of separate branches intersected
      by the cut determines the resulting clusters Advantages and Limitations Advantage the hierarchy can be
      examined at different levels of detail Advantage the number of clusters does not always need to be
      specified before building the hierarchy Limitation standard agglomerative methods can be computationally
      expensive for large datasets Limitation early merge or split decisions are generally not reversed 6 3
      Density Based Clustering DBSCAN DBSCAN stands for Density Based Spatial Clustering of Applications with
      Noise It forms clusters from dense regions of data and can identify isolated observations as noise Two
      Main Parameters Parameter Meaning Epsilon The maximum neighborhood distance used to decide which points
      are neighbors MinPts The minimum number of points required in the neighborhood for a point to be
      considered a core point DATA MINING WEEK 8 Week 8 Clustering Counting convention In the common DBSCAN
      convention the point itself is included when counting the points in its neighborhood A course or software
      implementation should state its convention explicitly Types of Points Point Type Meaning Core point Has at
      least MinPts points in its neighborhood including itself under the common convention Border point Has
      fewer than MinPts points in its own neighborhood but lies within the neighborhood of a core point Noise
      point Is not a core point and is not density reachable from a core point Basic DBSCAN Procedure 7 Select
      an unvisited point 8 Find all points within its neighborhood 9 If it has fewer than MinPts points in its
      neighborhood mark it as noise temporarily It may later be identified as a border point if it is reached
      from a core point 10 If it is a core point start a new cluster and expand the cluster through density
      reachable neighboring core points 11 Continue until all points have been visited Numerical Example Assume
      2 and MinPts 4 with the point itself included in the count If point P has three other points within
      distance 2 its neighborhood contains four points in total Therefore P is a core point If point Q has only
      one other point within distance 2 its neighborhood contains two points in total Q is not a core point it
      may be a border point if it is within the neighborhood of a core point Otherwise it is noise Advantages
      and Limitations Can discover clusters with irregular shapes Can identify noise and outliers Does not
      require the number of clusters to be specified in advance Choosing suitable and MinPts values can be
      difficult A single density setting may not work well when clusters have very different densities 6 4 Model
      Based Clustering Gaussian Mixture Model GMM A Gaussian Mixture Model assumes that the data are generated
      from a mixture of several Gaussian probability distributions Each Gaussian component represents one
      possible cluster Unlike K Means which assigns each object to one cluster GMM can provide a probability of
      membership for each object in each component This is called soft clustering Example A data object might
      have a 0 70 probability of belonging to Component 1 and a 0 30 probability of belonging to Component 2
      This expresses uncertainty about its cluster membership Expectation Maximization EM The Expectation
      Maximization algorithm is commonly used to estimate the parameters of a GMM 12 Initialization choose
      initial parameters for the Gaussian components DATA MINING WEEK 8 Week 8 Clustering 13 Expectation step E
      step estimate the probability that each data object belongs to each component 14 Maximization step M step
      update the component parameters using the estimated membership probabilities 15 Repeat the E step and M
      step until the model parameters or likelihood converge Important A Gaussian component is a mathematical
      component of the model It does not automatically correspond to a meaningful real world category
      interpretation requires examining the data 7 Determining the Number of Clusters Some clustering methods
      such as K Means require the number of clusters to be selected in advance Two commonly used evaluation
      approaches are the Elbow Method and the Silhouette Score 7 1 Elbow Method The Elbow Method runs K Means
      for several values of K and calculates the within cluster sum of squares WCSS for each value WCSS measures
      the sum of squared distances between data objects and the centroids of their assigned clusters Steps of
      the Elbow Method 16 Run K Means using K 1 2 3 and so on 17 Record the WCSS for each value of K 18 Plot K
      against WCSS 19 Look for a point where the decrease in WCSS begins to slow noticeably This point is called
      the elbow The elbow is a guide not a guaranteed mathematically optimal answer The choice should also
      consider the purpose of the analysis and whether the resulting clusters are useful 7 2 Silhouette Score
      The Silhouette Score measures how well an object fits within its assigned cluster compared with the
      nearest alternative cluster For an object i the Silhouette Score is s i b i a i max a i b i where a i is
      the average distance from object i to other objects in its own cluster and b i is the smallest average
      distance from object i to objects in another cluster the nearest neighboring cluster Silhouette Value
      Interpretation Close to 1 The object is well matched to its own cluster and separated from other clusters
      Around 0 The object is near a boundary between clusters Below 0 The object may be assigned to an
      unsuitable cluster The overall Silhouette Score is commonly calculated as the mean of the individual
      object scores A higher average score generally indicates better separated clusters but it should not be
      used alone
