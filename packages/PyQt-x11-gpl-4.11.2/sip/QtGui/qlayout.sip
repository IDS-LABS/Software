// qlayout.sip generated by MetaSIP on Thu Sep 11 18:36:31 2014
//
// This file is part of the QtGui Python extension module.
//
// Copyright (c) 2014 Riverbank Computing Limited <info@riverbankcomputing.com>
// 
// This file is part of PyQt.
// 
// This file may be used under the terms of the GNU General Public
// License versions 2.0 or 3.0 as published by the Free Software
// Foundation and appearing in the files LICENSE.GPL2 and LICENSE.GPL3
// included in the packaging of this file.  Alternatively you may (at
// your option) use any later version of the GNU General Public
// License if such license has been publicly approved by Riverbank
// Computing Limited (or its successors, if any) and the KDE Free Qt
// Foundation. In addition, as a special exception, Riverbank gives you
// certain additional rights. These rights are described in the Riverbank
// GPL Exception version 1.1, which can be found in the file
// GPL_EXCEPTION.txt in this package.
// 
// If you are unsure which license is appropriate for your use, please
// contact the sales department at sales@riverbankcomputing.com.
// 
// This file is provided AS IS with NO WARRANTY OF ANY KIND, INCLUDING THE
// WARRANTY OF DESIGN, MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE.


class QLayout : QObject, QLayoutItem
{
%TypeHeaderCode
#include <qlayout.h>
%End

public:
    enum SizeConstraint
    {
        SetDefaultConstraint,
        SetNoConstraint,
        SetMinimumSize,
        SetFixedSize,
        SetMaximumSize,
        SetMinAndMaxSize,
    };

    QLayout(QWidget *parent /TransferThis/);
    QLayout();
    virtual ~QLayout();
    int margin() const;
    int spacing() const;
    void setMargin(int);
    void setSpacing(int);
    bool setAlignment(QWidget *w, Qt::Alignment alignment);
    bool setAlignment(QLayout *l, Qt::Alignment alignment);
    void setAlignment(Qt::Alignment alignment);
    void setSizeConstraint(QLayout::SizeConstraint);
    QLayout::SizeConstraint sizeConstraint() const;
    void setMenuBar(QWidget *w /GetWrapper/);
%MethodCode
        Py_BEGIN_ALLOW_THREADS
        sipCpp->setMenuBar(a0);
        Py_END_ALLOW_THREADS
        
        // The layout's parent widget (if there is one) will now have ownership.
        QWidget *parent = sipCpp->parentWidget();
        
        if (a0 && parent)
        {
            PyObject *py_parent = sipGetPyObject(parent, sipType_QWidget);
            
            if (py_parent)
                sipTransferTo(a0Wrapper, py_parent);
        }
        else
        {
            // For now give the Python ownership to the layout.  This maintains
            // compatibility with previous versions and allows setMenuBar(QWidget()).
            sipTransferTo(a0Wrapper, sipSelf);
        }
%End

    QWidget *menuBar() const;
    QWidget *parentWidget() const;
    virtual void invalidate();
    virtual QRect geometry() const;
    bool activate();
    void update();
    void addWidget(QWidget *w /GetWrapper/);
%MethodCode
        Py_BEGIN_ALLOW_THREADS
        sipCpp->addWidget(a0);
        Py_END_ALLOW_THREADS
        
        // The layout's parent widget (if there is one) will now have ownership.
        QWidget *parent = sipCpp->parentWidget();
        
        if (parent)
        {
            PyObject *py_parent = sipGetPyObject(parent, sipType_QWidget);
            
            if (py_parent)
                sipTransferTo(a0Wrapper, py_parent);
        }
        else
        {
            // For now give the Python ownership to the layout.  This maintains
            // compatibility with previous versions and allows addWidget(QWidget()).
            sipTransferTo(a0Wrapper, sipSelf);
        }
%End

    virtual void addItem(QLayoutItem * /Transfer/) = 0;
    void removeWidget(QWidget *w);
    void removeItem(QLayoutItem * /TransferBack/);
    virtual Qt::Orientations expandingDirections() const;
    virtual QSize minimumSize() const;
    virtual QSize maximumSize() const;
    virtual void setGeometry(const QRect &);
    virtual QLayoutItem *itemAt(int index) const = 0;
    virtual QLayoutItem *takeAt(int index) = 0 /TransferBack/;
    virtual int indexOf(QWidget *) const;
    virtual int count() const = 0 /__len__/;
    virtual bool isEmpty() const;
    int totalHeightForWidth(int w) const;
    QSize totalMinimumSize() const;
    QSize totalMaximumSize() const;
    QSize totalSizeHint() const;
    virtual QLayout *layout();
    void setEnabled(bool);
    bool isEnabled() const;
    static QSize closestAcceptableSize(const QWidget *w, const QSize &s);

protected:
    void widgetEvent(QEvent *);
    virtual void childEvent(QChildEvent *e);
    void addChildLayout(QLayout *l /Transfer/);
    void addChildWidget(QWidget *w /GetWrapper/);
%MethodCode
        Py_BEGIN_ALLOW_THREADS
        #if defined(SIP_PROTECTED_IS_PUBLIC)
        sipCpp->addChildWidget(a0);
        #else
        sipCpp->sipProtect_addChildWidget(a0);
        #endif
        Py_END_ALLOW_THREADS
        
        // The layout's parent widget (if there is one) will now have ownership.
        QWidget *parent = sipCpp->parentWidget();
        
        if (parent)
        {
            PyObject *py_parent = sipGetPyObject(parent, sipType_QWidget);
        
            if (py_parent)
                sipTransferTo(a0Wrapper, py_parent);
        }
        else
        {
            // For now give the Python ownership to the layout.  This maintains
            // compatibility with previous versions and allows
            // addChildWidget(QWidget()).
            sipTransferTo(a0Wrapper, sipSelf);
        }
%End

    QRect alignmentRect(const QRect &) const;

public:
%If (Qt_4_3_0 -)
    void setContentsMargins(int left, int top, int right, int bottom);
%End
%If (Qt_4_3_0 -)
    void getContentsMargins(int *left, int *top, int *right, int *bottom) const;
%End
%If (Qt_4_3_0 -)
    QRect contentsRect() const;
%End
%If (Qt_4_6_0 -)
    void setContentsMargins(const QMargins &margins);
%End
%If (Qt_4_6_0 -)
    QMargins contentsMargins() const;
%End
%If (Qt_5_0_0 -)
    virtual QFlags<QSizePolicy::ControlType> controlTypes() const;
%End

private:
    QLayout(const QLayout &);
};
